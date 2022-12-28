import snowflake.connector
import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur_new = my_cnx.cursor() 
my_cur_new.execute("SELECT PIPELINE_START_TIME,CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION FROM SNOWVIEW_AUDIT_VW")
res_new=my_cur_new.fetchall()
df_new= pd.DataFrame(res_new, columns=[' PIPELINE_START_TIME','CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION'])
df_new = df_new.set_index('PIPELINE_START_TIME')
st.area_chart(df_new)
