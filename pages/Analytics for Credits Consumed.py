import plotly.express as px
import streamlit as st
st.set_page_config(layout="wide")
import snowflake.connector
import pandas as pd


my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])

my_cur = my_cnx.cursor() 
my_cur.execute("SELECT PIPELINE_NAME,SUM(CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION) AS CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION FROM SNOWVIEW_AUDIT_HISTORY GROUP BY PIPELINE_NAME")
res = my_cur.fetchall()
df= pd.DataFrame(res, columns=['PIPELINE NAME','CREDITS CONSUMED'])
fig = px.line(df, x="PIPELINE NAME", y="CREDITS CONSUMED", title='Credits Consumed by Pipelines')
fig.update_xaxes(titlefont=dict(family='Rockwell',color='crimson',size=10),tickfont=dict(family='Rockwell', size=7))
fig.update_yaxes(titlefont=dict(color='crimson',size=10))
#fig.update_xaxes(tickangle=90)
st.write(fig)

#my_cur1 = my_cnx.cursor() 
my_cur.execute("SELECT PIPELINE_START_TIME,CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION FROM SNOWVIEW_AUDIT_HISTORY ")
res=my_cur.fetchall()
df= pd.DataFrame(res, columns=['PIPELINE START TIME','CREDITS CONSUMED'])
fig = px.area(df, x='PIPELINE START TIME', y='CREDITS CONSUMED',title='Credits Consumed over Time Period')
fig.update_xaxes(titlefont=dict(family='Rockwell',color='crimson',size=10),tickfont=dict(family='Rockwell', size=10))
fig.update_yaxes(titlefont=dict(color='crimson',size=10))
st.write(fig)

#my_cur2 = my_cnx.cursor() 
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT PIPELINE_NAME,PIPELINE_EXECUTOR,PIPELINE_STATUS,PIPELINE_START_TIME,PIPELINE_END_TIME,PIPELINE_EXECUTION_TIME,CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION,ERROR_DETAILS FROM SNOWVIEW_AUDIT_HISTORY ORDER BY PIPELINE_START_TIME DESC")
res = my_cur.fetchall()
df= pd.DataFrame(res, columns=['Pipeline Name','Pipeline Executor','Pipeline Status','Pipeline Start Time','Pipeline End Time','Pipeline Execution Time (in seconds)','Credits Consumed','Error Details'])
fig = px.pie(df, values='Credits Consumed', names='Pipeline Name',title='Credits Consumed by Pipelines')
fig.update_traces(textposition='inside')
fig.update_layout(legend_title_text='Pipeline Names')
fig.update_layout(showlegend=True, legend=dict(
    title_font_family='Courier New',
    font=dict(
        size=8
    )
))
st.write(fig)



