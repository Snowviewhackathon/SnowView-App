import snowflake.connector
import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
import plotly.express as px


my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor() 
my_cur.execute("SELECT PIPELINE_NAME,SUM(CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION) AS CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION FROM SNOWVIEW_AUDIT_VW GROUP BY PIPELINE_NAME")
res = my_cur.fetchall()
df= pd.DataFrame(res, columns=['PIPELINE NAME','CREDITS CONSUMED'])
fig = px.line(df, x="PIPELINE NAME", y="CREDITS CONSUMED", title='Analytics for Credits consumed')
#fig.update_xaxes(ticks="inside")
fig.update_xaxes(titlefont=dict(color='crimson',size=10),tickfont=dict(family='Rockwell', size=5))
#fig.update_yaxes(ticks="inside", col=1)
   
st.write(fig)

