import streamlit
import requests
import pandas
import snowflake.connector
import base64
from urllib.error import URLError
#from PIL import image

#streamlit.title('Snow View')
#streamlit.success('Snow View')
#streamlit.markdown('Snowflake Process : Execution Details')
streamlit.markdown(f'<h1 style="color:#1874CD;font-size:32px;">{"Snow View"}</h1>', unsafe_allow_html=True)
streamlit.markdown(f'<h1 style="color:#6495ED;font-size:24px;">{"Execution Details"}</h1>', unsafe_allow_html=True)
#img = image.open("snowview_img1.jpg");

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor() 
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT PIPELINE_NAME,PIPELINE_EXECUTOR,PIPELINE_STATUS,PIPELINE_START_TIME,PIPELINE_END_TIME,PIPELINE_EXECUTION_TIME,CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION,ERROR_DETAILS FROM SNOWVIEW_AUDIT_VW")
my_data_row = my_cur.fetchall()
#columns = ('colm1','colm2','colm3','colm4','colm5','colm6','colm7','colm8')
#columns=('col %d' % i for i in range(8)))
#streamlit.dataframe(my_data_row) 
streamlit.table(my_data_row) 
