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
fig.update_layout(
    autosize=False,
    width=500,
    height=500,
    yaxis=dict(
            titlefont=dict(size=10),
    xaxis=dict(
            titlefont=dict(size=10),
            #tickfont=list(size=10),
        ))
st.write(fig)

