import snowflake.connector
import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
import plotly.express as px


my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor() 
my_cur.execute("SELECT PIPELINE_NAME,SUM(PIPELINE_EXECUTION_TIME) AS PIPELINE_EXECUTION_TIME FROM SNOWVIEW_AUDIT_HISTORY GROUP BY PIPELINE_NAME")
res = my_cur.fetchall()
df= pd.DataFrame(res, columns=['PIPELINE NAME','PIPELINE EXECUTION TIME(in seconds)'])
fig = px.line(df, x="PIPELINE NAME", y="PIPELINE EXECUTION TIME(in seconds)", title='Analytics for Pipeline Execution time')
fig.update_xaxes(titlefont=dict(family='Rockwell',color='crimson',size=10),tickfont=dict(family='Rockwell', size=7))
fig.update_yaxes(titlefont=dict(color='crimson',size=10))  
st.write(fig)


my_cur2 = my_cnx.cursor() 
my_cur2.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur2.execute("SELECT PIPELINE_NAME,PIPELINE_EXECUTION_TIME FROM SNOWVIEW_AUDIT_HISTORY ORDER BY PIPELINE_START_TIME DESC")
res2 = my_cur2.fetchall()
df2= pd.DataFrame(res2, columns=['Pipeline Name','Pipeline Execution Time (in seconds)'])
fig1 = px.pie(df2, values='Pipeline Execution Time (in seconds)', names='Pipeline Name',title='Analytics for Pipeline Execution time')
fig1.update_traces(textposition='inside')
fig1.update_layout(legend_title_text='Pipeline Names')
fig1.update_layout(showlegend=True, legend=dict(
    title_font_family='Courier New',
    font=dict(
        size=8
    )
))
st.write(fig1)
