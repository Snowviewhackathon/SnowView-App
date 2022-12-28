import plotly.express as px
import streamlit as st
import snowflake.connector
import pandas as pd


my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor() 
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT PIPELINE_NAME,PIPELINE_EXECUTOR,PIPELINE_STATUS,PIPELINE_START_TIME,PIPELINE_END_TIME,PIPELINE_EXECUTION_TIME,CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION,ERROR_DETAILS FROM SNOWVIEW_AUDIT_HISTORY ORDER BY PIPELINE_START_TIME DESC")
res = my_cur.fetchall()
df= pd.DataFrame(res, columns=['Pipeline Name','Pipeline Executor','Pipeline Status','Pipeline Start Time','Pipeline End Time','Pipeline Execution Time (in seconds)','Credits Consumed','Error Details'])

fig = px.pie(df, values='Credits Consumed', names='Pipeline Name',title='Analytics for Credits consumed')
fig1 = px.pie(df, values='Pipeline Execution Time (in seconds)', names='Pipeline Name',title='Analytics for Pipeline Execution time')
fig.update_traces(textposition='inside')
fig1.update_traces(textposition='inside')
fig.update_layout(legend_title_text='Pipeline Names')
fig1.update_layout(legend_title_text='Pipeline Names')
fig.update_layout(showlegend=True, legend=dict(
    title_font_family='Courier New',
    font=dict(
        size=8
    )
))
fig1.update_layout(showlegend=True, legend=dict(
    title_font_family='Courier New',
    font=dict(
        size=8
    )
))
st.write(fig)
st.write(fig1)
