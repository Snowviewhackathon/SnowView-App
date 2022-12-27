import snowflake.connector
import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
import altair as alt
import numpy as np

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor() 
my_cur_new = my_cnx.cursor() 
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_cur.execute("SELECT PIPELINE_NAME,PIPELINE_EXECUTOR,PIPELINE_STATUS,PIPELINE_START_TIME,PIPELINE_END_TIME,PIPELINE_EXECUTION_TIME,CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION,ERROR_DETAILS FROM SNOWVIEW_AUDIT_VW")
my_cur.execute("SELECT PIPELINE_NAME,CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION FROM SNOWVIEW_AUDIT_VW")
my_cur_new.execute("SELECT PIPELINE_START_TIME,CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION FROM SNOWVIEW_AUDIT_VW")
res = my_cur.fetchall()
res_new=my_cur_new.fetchall()
#df= pd.DataFrame(res, columns=['Pipeline Name','Pipeline Executor','Pipeline Status','Pipeline Start Time','Pipeline End Time','Pipeline Execution Time (in seconds)','Credits Consumed','Error Details'])
df= pd.DataFrame(res, columns=['PIPELINE_NAME','CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION'])
df_new= pd.DataFrame(res_new, columns=[' PIPELINE_START_TIME','CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION'])
#st.area_chart(df)
#df = df.set_index('PIPELINE_NAME')
df_new = df_new.set_index(' PIPELINE_START_TIME')
#st.line_chart(df,width = 10)

#st.area_chart(df_new)



c = alt.Chart(df, title='Credits consumed by piplines').mark_line().encode(x='PIPELINE',y='Credits', color='parameter')

st.altair_chart(c, use_container_width=True)




