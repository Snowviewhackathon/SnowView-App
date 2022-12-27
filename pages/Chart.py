import snowflake.connector
import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor() 
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_cur.execute("SELECT PIPELINE_NAME,PIPELINE_EXECUTOR,PIPELINE_STATUS,PIPELINE_START_TIME,PIPELINE_END_TIME,PIPELINE_EXECUTION_TIME,CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION,ERROR_DETAILS FROM SNOWVIEW_AUDIT_VW")
my_cur.execute("SELECT PIPELINE_NAME,CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION FROM SNOWVIEW_AUDIT_VW")
res = my_cur.fetchall()
#df= pd.DataFrame(res, columns=['Pipeline Name','Pipeline Executor','Pipeline Status','Pipeline Start Time','Pipeline End Time','Pipeline Execution Time (in seconds)','Credits Consumed','Error Details'])
df= pd.DataFrame(res, columns=['PIPELINE_NAME','CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION'])
#st.area_chart(df)
df = df.set_index('PIPELINE_NAME')
st.line_chart(df,use_container_width=True)




