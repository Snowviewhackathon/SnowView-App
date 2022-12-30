import plotly.express as px
import streamlit as st
st.set_page_config(layout="wide")
import snowflake.connector
import pandas as pd
import altair as alt


my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])

my_cur = my_cnx.cursor() 
my_cur.execute("SELECT PIPELINE_NAME,SUM(CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION) AS CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION FROM SNOWVIEW_AUDIT_VW GROUP BY PIPELINE_NAME")
res = my_cur.fetchall()
df= pd.DataFrame(res, columns=['PIPELINE NAME','CREDITS CONSUMED'])





c = alt.Chart(df, title='measure of different elements over time').mark_line().encode(
     x='PIPELINE NAME', y='CREDITS CONSUMED')

st.altair_chart(c, use_container_width=True)
