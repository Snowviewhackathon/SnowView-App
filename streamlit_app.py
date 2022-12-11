import streamlit
import requests
import pandas
import snowflake.connector
from urllib.error import URLError

streamlit.title('Snow View')
streamlit.header('Metadata Details')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.dataframe(my_data_row)
