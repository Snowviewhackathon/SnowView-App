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

fig = px.pie(df, values='Credits Consumed', names='Pipeline Name',title='Pipeline Name and Credits Consumed')
fig1 = px.pie(df, values='Credits Consumed', names='Pipeline Status',title='Pipeline Status and Credits Consumed')
fig.update_traces(textposition='inside')
#fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
#fig.show()
st.write(fig)
st.write(fig1)
