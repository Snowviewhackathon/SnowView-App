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
st.write(df)
#df_nxt = df.drop_duplicates(subset='Pipeline Start Time')
df_wide = df.pivot(index ='PIPELINE_START_TIME', columns = 'PIPELINE_NAME', values = 'CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION').reset_index()
st.write(df_wide)
fig1 = px.line(
    data_frame = df_wide
    ,x = 'PIPELINE_START_TIME'
    ,y = ['Snowpark : Snowpark Python Code','Task : TASK_LOAD_AUDIT_HISTORY','Task : TASK_SP_LOAD_CSV_EXTERNAL_STAGE']
)
 
#fig1.show()
st.write(fig1)

