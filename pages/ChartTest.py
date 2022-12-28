import snowflake.connector
import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
import plotly.express as px


my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor() 
my_cur.execute("SELECT PIPELINE_NAME,PIPELINE_START_TIME,CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION FROM SNOWVIEW_AUDIT_VW")
res = my_cur.fetchall()
df= pd.DataFrame(res, columns=['PIPELINE_NAME','PIPELINE_START_TIME','CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION'])
my_cur.execute("SELECT PIPELINE_NAME,SUM(CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION) CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION FROM SNOWVIEW_AUDIT_VW GROUP BY PIPELINE_NAME")
res = my_cur.fetchall()
df= pd.DataFrame(res)
st.write(res)
#df_nxt = df.drop_duplicates(subset='Pipeline Start Time')
df_wide = df.pivot(index ='PIPELINE_START_TIME', columns = 'PIPELINE_NAME',  values = 'CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION').reset_index()
#st.write(df_wide)
fig1 = px.line(
    data_frame = df_wide
    ,x = 'PIPELINE_START_TIME'
    ,y = ['Snowpark : Snowpark Python Code','Task : TASK_LOAD_AUDIT_HISTORY','Task : TASK_SP_LOAD_CSV_EXTERNAL_STAGE']
)
fig3 = px.line(
    data_frame = df
    ,x = 'PIPELINE_START_TIME'
    ,y = 'CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION'
    ,color = 'PIPELINE_NAME'
)
 
#fig3.show()
#fig1.show()
st.write(fig1)
st.write(fig3)

