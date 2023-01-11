import snowflake.connector
import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
import plotly.express as px


my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor() 
#my_cur.execute("select * from pipeline_execution_time_vw")
my_cur.execute("SELECT PIPELINE_NAME,SUM(PIPELINE_EXECUTION_TIME) AS PIPELINE_EXECUTION_TIME FROM SNOWVIEW_AUDIT_VW GROUP BY PIPELINE_NAME")
res = my_cur.fetchall()
df= pd.DataFrame(res, columns=['PIPELINE NAME','PIPELINE EXECUTION TIME(in seconds)'])
fig = px.line(df, x="PIPELINE NAME", y="PIPELINE EXECUTION TIME(in seconds)", title='Analytics for Pipeline Execution time')
fig.update_xaxes(titlefont=dict(family='Rockwell',color='crimson',size=10),tickfont=dict(family='Rockwell', size=7))
fig.update_yaxes(titlefont=dict(color='crimson',size=10))  
st.write(fig)
