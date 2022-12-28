import snowflake.connector
import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
import plotly.express as px


my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor() 
my_cur.execute("SELECT PIPELINE_NAME,PIPELINE_START_TIME,CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION FROM SNOWVIEW_AUDIT_VW")
res = my_cur.fetchall()
#df= pd.DataFrame(res, columns=['Pipeline Name','Pipeline Executor','Pipeline Status','Pipeline Start Time','Pipeline End Time','Pipeline Execution Time (in seconds)','Credits Consumed','Error Details'])
df= pd.DataFrame(res, columns=['PIPELINE_NAME','Pipeline Start Time','CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION'])
#df = df.set_index('PIPELINE_NAME')
st.write(df)
df_nxt = df.drop_duplicates(subset='Pipeline Start Time')
df_wide = df_nxt.pivot(index = 'Pipeline Start Time', columns = 'PIPELINE_NAME', values = 'CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION').reset_index()
st.write(df_wide)
fig1 = px.line(
    data_frame = df_wide
    ,x = 'Pipeline Start Time'
    ,y = ['Snowpark : Snowpark Python Code','Task : TASK_LOAD_AUDIT_HISTORY','Task : TASK_SP_LOAD_CSV_EXTERNAL_STAGE','Task : TASK_SP_LOAD_CSV_INTERNAL_STAGE']
)
 
#fig1.show()
st.write(fig1)
my_cur_new = my_cnx.cursor() 
#my_cur.execute("SELECT PIPELINE_NAME,PIPELINE_EXECUTOR,PIPELINE_STATUS,PIPELINE_START_TIME,PIPELINE_END_TIME,PIPELINE_EXECUTION_TIME,CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION,ERROR_DETAILS FROM SNOWVIEW_AUDIT_VW")
my_cur_new.execute("SELECT PIPELINE_START_TIME,PIPELINE_STATUS,CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION FROM SNOWVIEW_AUDIT_VW")
res_new=my_cur_new.fetchall()
df_new= pd.DataFrame(res_new, columns=[' PIPELINE_START_TIME','PIPELINE_STATUS','CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION'])
df_wide = df_new.pivot(index = 'PIPELINE_START_TIME', columns = 'PIPELINE_STATUS', values = 'CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION').reset_index()
st.write(df_wide)
fig2 = px.line(
    data_frame = df_wide
    ,x = 'Pipeline Start Time'
    ,y = ['Snowpark : Snowpark Python Code','Task : TASK_LOAD_AUDIT_HISTORY','Task : TASK_SP_LOAD_CSV_EXTERNAL_STAGE','Task : TASK_SP_LOAD_CSV_INTERNAL_STAGE']
)
 
#fig1.show()
st.write(fig2)



