import snowflake.connector
import streamlit as st
import plotly.express as px
st.set_page_config(layout="wide")
import pandas as pd

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur_new = my_cnx.cursor() 
my_cur_new.execute("SELECT PIPELINE_EXECUTION_TIME,CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION FROM SNOWVIEW_AUDIT_VW ")
res_new=my_cur_new.fetchall()
df_new= pd.DataFrame(res_new, columns=['PIPELINE EXECUTION TIME','CREDITS CONSUMED'])
fig = px.area(df_new, x='PIPELINE EXECUTION TIME', y='CREDITS CONSUMED',title='Analytics for Credits consumed_area_chart')
fig.update_xaxes(titlefont=dict(family='Rockwell',color='crimson',size=10),tickfont=dict(family='Rockwell', size=5))
fig.update_yaxes(titlefont=dict(color='crimson',size=10))

st.write(fig)
