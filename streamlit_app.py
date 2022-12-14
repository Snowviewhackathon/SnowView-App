import streamlit
import requests
import pandas as pd
import snowflake.connector
import base64
from urllib.error import URLError
#from PIL import image


def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    streamlit.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://i.pinimg.com/564x/03/f5/14/03f5147b9a374dc1944495a66d1f256b.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    
set_bg_hack_url() 

#streamlit.title('Snow View')
#streamlit.success('Snow View')
#streamlit.markdown('Snowflake Process : Execution Details')
streamlit.markdown(f'<h1 style="color:#1874CD;font-size:40px;">{"Snow View"}</h1>', unsafe_allow_html=True)
streamlit.markdown(f'<h1 style="color:#6495ED;font-size:24px;">{"Snowflake Process : Execution Details"}</h1>', unsafe_allow_html=True)
#img = image.open("snowview_img1.jpg");

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor() 
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT PIPELINE_NAME,PIPELINE_EXECUTOR,PIPELINE_STATUS,PIPELINE_START_TIME,PIPELINE_END_TIME,PIPELINE_EXECUTION_TIME,CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION,ERROR_DETAILS FROM SNOWVIEW_AUDIT_VW")
res = my_cur.fetchall()
df= pd.DataFrame(res, columns=['PIPELINE_NAME','PIPELINE_EXECUTOR','PIPELINE_STATUS','PIPELINE_START_TIME','PIPELINE_END_TIME','PIPELINE_EXECUTION_TIME','CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION','ERROR_DETAILS'])

streamlit.dataframe(df,1000,500)
#a=df.style.set_properties(**{'border': '1.3px solid green','color': 'magenta'})
##s=df.style.set_table_styles([
#                            {
#                               "selector":"thead",
#                                "props":"background-color:skyblue; color:white; border:1.3px solid black;"
#                            },
#
#                       ])
#

##type(s)
##streamlit.table(s) 

#columns = ('colm1','colm2','colm3','colm4','colm5','colm6','colm7','colm8')
#columns=('col %d' % i for i in range(8)))
#streamlit.dataframe(my_data_row)
