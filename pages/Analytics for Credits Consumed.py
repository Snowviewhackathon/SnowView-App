import plotly.express as px
import streamlit as st
st.set_page_config(layout="wide")
import snowflake.connector
import pandas as pd


my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])

my_cur = my_cnx.cursor() 
my_cur.execute("select * from pipeline_credits_consumed_vw")
#my_cur.execute("SELECT PIPELINE_NAME,SUM(CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION) AS CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION FROM SNOWVIEW_AUDIT_VW GROUP BY PIPELINE_NAME")
res = my_cur.fetchall()
df= pd.DataFrame(res, columns=['PIPELINE NAME','CREDITS CONSUMED'])
fig = px.line(df, x="PIPELINE NAME", y="CREDITS CONSUMED", title='Credits Consumed by Pipelines')
fig.update_xaxes(titlefont=dict(family='Rockwell',color='crimson',size=10),tickfont=dict(family='Rockwell', size=10))
fig.update_yaxes(titlefont=dict(color='crimson',size=10))
#fig.update_xaxes(tickangle=90)
st.write(fig)

my_cur1 = my_cnx.cursor() 
my_cur1.execute("SELECT PIPELINE_START_TIME,CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION FROM SNOWVIEW_AUDIT_VW ")
res1=my_cur1.fetchall()
df1= pd.DataFrame(res1, columns=['PIPELINE START TIME','CREDITS CONSUMED'])
fig1 = px.area(df1, x='PIPELINE START TIME', y='CREDITS CONSUMED',title='Credits Consumed over Time Period')
fig1.update_xaxes(titlefont=dict(family='Rockwell',color='crimson',size=10),tickfont=dict(family='Rockwell', size=10))
fig1.update_yaxes(titlefont=dict(color='crimson',size=10))
#st.write(fig)
st.write(fig1)

my_cur2 = my_cnx.cursor() 
#my_cur2.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur2.execute("select * from pipeline_credits_consumed_vw")
#my_cur2.execute("SELECT PIPELINE_NAME,PIPELINE_EXECUTOR,PIPELINE_STATUS,PIPELINE_START_TIME,PIPELINE_END_TIME,PIPELINE_EXECUTION_TIME,CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION,ERROR_DETAILS FROM SNOWVIEW_AUDIT_HISTORY ORDER BY PIPELINE_START_TIME DESC")
res2 = my_cur2.fetchall()
df2= pd.DataFrame(res2, columns=['Pipeline Name','Credits Consumed'])
fig2 = px.pie(df2, values='Credits Consumed', names='Pipeline Name',title='Credits Consumed by Pipelines')
fig2.update_traces(textposition='inside')
fig2.update_layout(legend_title_text='Pipeline Names')
fig2.update_layout(showlegend=True, legend=dict(
    title_font_family='Courier New',
    font=dict(
        size=8
    )
))
st.write(fig2)



