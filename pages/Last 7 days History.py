import streamlit
import pandas as pd
import snowflake.connector

streamlit.markdown(
     f"""
     <style>
     .stApp {{
         #background: url("");
         background-color: PaleGreen;
         background-size: cover
     }}
     </style>
     """,
     unsafe_allow_html=True
 )
streamlit.markdown(f'<h1 style="color:#6495ED;font-size:24px;">{"Snowflake Process : Execution Details"}</h1>', unsafe_allow_html=True)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor() 
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT PIPELINE_NAME,PIPELINE_EXECUTOR,PIPELINE_STATUS,PIPELINE_START_TIME,PIPELINE_END_TIME,PIPELINE_EXECUTION_TIME,CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION,ERROR_DETAILS FROM SNOWVIEW_AUDIT_VW")
res = my_cur.fetchall()
df= pd.DataFrame(res, columns=['Pipeline Name','Pipeline Executor','Pipeline Status','Pipeline Start Time','Pipeline End Time','Pipeline Execution Time','Credits Consumed','Error Details'])

res=df.style.set_table_styles([
                            {
                               "selector":"thead",
                                "props":"font-weight:800; font-size:16px; color:#000000; background-color: LightGreen; border:1.1px black;"
                            },
                            {
                               "selector":"td",
                                "props":"font-size:11px"
                            },
                          
                            {
                               "selector":"stTable",
                                "props":"width:100%;"
                            },

                       ])

type(res)
streamlit.table(res) 
