import plotly.express as px
import streamlit as st
st.set_page_config(layout="wide")
import snowflake.connector
import pandas as pd


my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])

my_cur = my_cnx.cursor() 

#my_cur2.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from pipeline_credits_consumed_vw")
#my_cur2.execute("SELECT PIPELINE_NAME,PIPELINE_EXECUTOR,PIPELINE_STATUS,PIPELINE_START_TIME,PIPELINE_END_TIME,PIPELINE_EXECUTION_TIME,CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION,ERROR_DETAILS FROM SNOWVIEW_AUDIT_HISTORY ORDER BY PIPELINE_START_TIME DESC")
res2 = my_cur.fetchall()
df2= pd.DataFrame(res2, columns=['Pipeline Name','Credits Consumed'])
fig2 = px.pie(df2, values='Credits Consumed', names='Pipeline Name',title='Credits Consumed by Pipelines')
fig2.update_traces(textposition='inside')
fig2.update_layout(legend_title_text='Pipeline Names')
fig2.update_layout(showlegend=True, legend=dict(
    title_font_family='Courier New',
    font=dict(
        size=10
    )
))
st.write(fig2)

#my_cur2 = my_cnx.cursor() 
#my_cur2.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from pipeline_execution_time_vw")
#my_cur2.execute("SELECT PIPELINE_NAME,PIPELINE_EXECUTION_TIME FROM SNOWVIEW_AUDIT_HISTORY ORDER BY PIPELINE_START_TIME DESC")
res2 = my_cur.fetchall()
df2= pd.DataFrame(res2, columns=['Pipeline Name','Pipeline Execution Time (in seconds)'])
fig1 = px.pie(df2, values='Pipeline Execution Time (in seconds)', names='Pipeline Name',title='Analytics for Pipeline Execution time')
fig1.update_traces(textposition='inside')
fig1.update_layout(legend_title_text='Pipeline Names')
fig1.update_layout(showlegend=True, legend=dict(
    title_font_family='Courier New',
    font=dict(
        size=10
    )
))
st.write(fig1)
