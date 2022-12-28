import snowflake.connector
import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur_new = my_cnx.cursor() 
my_cur_new.execute("SELECT PIPELINE_NAME,SUM(PIPELINE_EXECUTION_TIME) AS PIPELINE_EXECUTION_TIME FROM SNOWVIEW_AUDIT_VW GROUP BY PIPELINE_NAME")
res_new=my_cur_new.fetchall()
df_new= pd.DataFrame(res_new, columns=['PIPELINE NAME','PIPELINE EXECUTION TIME'])
fig = px.area(df_new, x='PIPELINE NAME', y='PIPELINE EXECUTION TIME')

st.write(fig)
