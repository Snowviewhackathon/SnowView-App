import snowflake.connector
import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
import altair as alt

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor() 
my_cur_new = my_cnx.cursor() 
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_cur.execute("SELECT PIPELINE_NAME,PIPELINE_EXECUTOR,PIPELINE_STATUS,PIPELINE_START_TIME,PIPELINE_END_TIME,PIPELINE_EXECUTION_TIME,CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION,ERROR_DETAILS FROM SNOWVIEW_AUDIT_VW")
my_cur.execute("SELECT PIPELINE_NAME,CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION FROM SNOWVIEW_AUDIT_VW")
my_cur_new.execute("SELECT PIPELINE_START_TIME,CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION FROM SNOWVIEW_AUDIT_VW")
res = my_cur.fetchall()
res_new=my_cur_new.fetchall()
#df= pd.DataFrame(res, columns=['Pipeline Name','Pipeline Executor','Pipeline Status','Pipeline Start Time','Pipeline End Time','Pipeline Execution Time (in seconds)','Credits Consumed','Error Details'])
df= pd.DataFrame(res, columns=['PIPELINE_NAME','CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION'])
df_new= pd.DataFrame(res_new, columns=[' PIPELINE_START_TIME','CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION'])
#st.area_chart(df)
df = df.set_index('PIPELINE_NAME')
df_new = df_new.set_index(' PIPELINE_START_TIME')
st.line_chart(df,width = 10, height = 210,use_container_width=True)

st.area_chart(df_new)


df = pd.DataFrame(
                np.random.rand(10, 4),
                columns= ["NO2","C2H5CH","VOC","CO"])
# generate a date range to be used as the x axis
df['date'] =  pd.date_range("2014-01-01", periods=10, freq="m")
df_melted = pd.melt(df,id_vars=['date'],var_name='parameter', value_name='value')
c = alt.Chart(df_melted, title='measure of different elements over time').mark_line().encode(
     x='date', y='value', color='parameter')

st.altair_chart(c, use_container_width=True)




