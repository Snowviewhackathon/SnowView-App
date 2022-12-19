import streamlit as st
# Import pandas library
import pandas as pd
 
# initialize list of lists
data = [['tom', 10], ['nick', 15], ['juli', 14]]
 
# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age'])

 
#st.dataframe(filter_dataframe(df.style.set_properties(**{'font-size':'24pt'})))
st.dataframe(df.style.set_properties(**{'background-color': 'black','color': 'green','font-size':'5rem'}))                                                       


