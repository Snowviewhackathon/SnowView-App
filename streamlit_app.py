import streamlit
#import cv2
import requests
import pandas
import snowflake.connector
from urllib.error import URLError

original_title = '<p style="font-family:Courier; color:Blue; font-size: 30px;">Snow View</p>'
st.markdown(original_title, unsafe_allow_html=True)
#streamlit.title('Snow View')
#streamlit.header('Metadata Details')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from snowview_audit_vw")
my_data_row = my_cur.fetchall()
streamlit.dataframe(my_data_row)
