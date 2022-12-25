import plotly.express as px
import streamlit as st
import plotly.express as px
import snowflake.connector
import pandas as pd

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor() 
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT PIPELINE_NAME,PIPELINE_EXECUTOR,PIPELINE_STATUS,PIPELINE_START_TIME,PIPELINE_END_TIME,PIPELINE_EXECUTION_TIME,CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION,ERROR_DETAILS FROM SNOWVIEW_AUDIT_HISTORY ORDER BY PIPELINE_START_TIME DESC")
res = my_cur.fetchall()
df= pd.DataFrame(res, columns=['Pipeline Name','Pipeline Executor','Pipeline Status','Pipeline Start Time','Pipeline End Time','Pipeline Execution Time (in seconds)','Credits Consumed','Error Details'])

# This dataframe has 244 lines, but 4 distinct values for `day`
#df = px.data.res()
fig = px.pie(df, values='Credits Consumed', names='Pipeline Name')
#fig.show()
st.write(fig)


a=df.groupby('Pipeline Status')['Pipeline Status'].count().plot.pie(autopct='%.2f',figsize=(5,5))


st.dataframe(a)

