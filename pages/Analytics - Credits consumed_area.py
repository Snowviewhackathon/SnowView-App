import snowflake.connector
import streamlit as st
import plotly.express as px
st.set_page_config(layout="wide")
import pandas as pd

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur_new = my_cnx.cursor() 
my_cur_new.execute("SELECT PIPELINE_NAME,SUM(PIPELINE_EXECUTION_TIME) AS PIPELINE_EXECUTION_TIME FROM SNOWVIEW_AUDIT_VW GROUP BY PIPELINE_NAME")
res_new=my_cur_new.fetchall()
df_new= pd.DataFrame(res_new, columns=['PIPELINE NAME','PIPELINE EXECUTION TIME'])
fig = px.area(df_new, x='PIPELINE NAME', y='PIPELINE EXECUTION TIME',title='Analytics for Credits consumed_area_chart')
fig.update_xaxes(titlefont=dict(family='Rockwell',color='crimson',size=10),tickfont=dict(family='Rockwell', size=5))
fig.update_yaxes(titlefont=dict(color='crimson',size=10))

st.write(fig)
