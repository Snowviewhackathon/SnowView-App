import snowflake.connector
import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
import plotly.express as px


my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor() 
my_cur.execute("SELECT PIPELINE_NAME,SUM(CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION) CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION FROM SNOWVIEW_AUDIT_VW GROUP BY PIPELINE_NAME")
res = my_cur.fetchall()
df= pd.DataFrame(res, columns=['PIPELINE_NAME','CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION'])
fig = px.line(
    data_frame = df
    ,x = 'PIPELINE_NAME'
    ,y = 'CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION'
    ,color = 'PIPELINE_NAME'
)
 
st.write(fig)
