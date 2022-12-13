import streamlit
import requests
import pandas
import snowflake.connector
from urllib.error import URLError

streamlit.title('Snow View')
#streamlit.success('Snow View')
streamlit.markdown('Execution Details')
img = image.open("snowview_img1.jpg");

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT PIPELINE_NAME,PIPELINE_EXECUTOR,PIPELINE_STATUS,ERROR_DETAILS,PIPELINE_START_TIME,PIPELINE_END_TIME,PIPELINE_EXECUTION_TIME,CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION FROM SNOWVIEW_AUDIT_VW")
my_data_row = my_cur.fetchall()
#streamlit.dataframe(my_data_row) 
streamlit.dataframe(my_data_row) 
