import snowflake.connector
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor() 
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT PIPELINE_NAME,PIPELINE_EXECUTOR,PIPELINE_STATUS,PIPELINE_START_TIME,PIPELINE_END_TIME,PIPELINE_EXECUTION_TIME,CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION,ERROR_DETAILS FROM SNOWVIEW_AUDIT_VW")
res = my_cur.fetchall()
df= pd.DataFrame(res, columns=['Pipeline Name','Pipeline Executor','Pipeline Status','Pipeline Start Time','Pipeline End Time','Pipeline Execution Time (in seconds)','Credits Consumed','Error Details'])
st.markdown(f'<h1 style="color:#FFFFFF;font-size:48px;">{"❄️SnowView"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#FFFFFF;font-size:24px;text-align: center;">{"Chart"}</h1>', unsafe_allow_html=True)   
st.markdown(
     f"""
     <style>
     .stApp {{
         #background: url("");
         background-color: #86b6fd;
         #background-size: cover
     }}
     </style>
     """,
     unsafe_allow_html=True
 )
st.dataframe(filter_dataframe(df))
