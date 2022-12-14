import streamlit
import requests
import pandas as pd
import snowflake.connector
import base64
from urllib.error import URLError
#from PIL import image

#streamlit.title('Snow View')
#streamlit.success('Snow View')
#streamlit.markdown('Snowflake Process : Execution Details')
streamlit.markdown(f'<h1 style="color:#1874CD;font-size:40px;">{"Snow View"}</h1>', unsafe_allow_html=True)
streamlit.markdown(f'<h1 style="color:#6495ED;font-size:24px;">{"Snowflake Process : Execution Details"}</h1>', unsafe_allow_html=True)
streamlit.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://images.app.goo.gl/LFCobouKtT7oZ7Qv7")
    }
   .sidebar .sidebar-content {
        background: url("https://images.app.goo.gl/LFCobouKtT7oZ7Qv7")
    }
    </style>
    """,
    unsafe_allow_html=True
)
#img = image.open("snowview_img1.jpg");

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor() 
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT PIPELINE_NAME,PIPELINE_EXECUTOR,PIPELINE_STATUS,PIPELINE_START_TIME,PIPELINE_END_TIME,PIPELINE_EXECUTION_TIME,CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION,ERROR_DETAILS FROM SNOWVIEW_AUDIT_VW")
res = my_cur.fetchall()
df = pd.DataFrame(res, columns=['PIPELINE_NAME','PIPELINE_EXECUTOR','PIPELINE_STATUS','PIPELINE_START_TIME','PIPELINE_END_TIME','PIPELINE_EXECUTION_TIME','CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION','ERROR_DETAILS'])
#a=df.style.set_properties(**{'background-color': 'blue','color': 'black'})
#a=df.style
a=df.style.set_properties(**{'border': '1.3px solid green','color': 'magenta'})

#streamlit.markdown(page_bg_img, unsafe_allow_html=True)
streamlit.table(a)

#columns = ('colm1','colm2','colm3','colm4','colm5','colm6','colm7','colm8')
#columns=('col %d' % i for i in range(8)))
#streamlit.dataframe(my_data_row)
