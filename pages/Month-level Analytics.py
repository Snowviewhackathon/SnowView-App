import snowflake.connector
import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
import plotly.express as px


my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor() 
my_cur.execute("SELECT * from MONTHLY_CREDITS_CONSUMED_VIEW")
res = my_cur.fetchall()
df= pd.DataFrame(res, columns=['MONTH','CREDITS CONSUMED']) 
fig = px.bar(df, x="MONTH", y="CREDITS CONSUMED",  title="Month-level Analytics for Credits Consumed")
fig.update_xaxes(titlefont=dict(family='Rockwell',color='crimson',size=10),tickfont=dict(family='Rockwell', size=9))
fig.update_yaxes(titlefont=dict(color='crimson',size=10))
st.write(fig)

my_cur.execute("SELECT * from MONTHLY_PIPELINE_EXECUTION_VIEW")
res = my_cur.fetchall()
df= pd.DataFrame(res, columns=['MONTH','PIPELINE EXECUTION TIME(in hour)']) 
fig = px.bar(df, x="MONTH", y="PIPELINE EXECUTION TIME(in hour)",  title="Month-level Analytics for Pipeline Execution Time")
fig.update_xaxes(titlefont=dict(family='Rockwell',color='crimson',size=10),tickfont=dict(family='Rockwell', size=8))
fig.update_yaxes(titlefont=dict(color='crimson',size=10))
st.write(fig)
