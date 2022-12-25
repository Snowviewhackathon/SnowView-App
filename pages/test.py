import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth 

import pandas as pd

data = {
  "A": [420, 380, 390],
  "B": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 
#st.dataframe(df.style.highlight_max(axis=0, props='background-color:green;', subset=['A','B'])
         #.highlight_min(axis=0, props='background-color:red;', subset=['A','B']))
#st.dataframe(df)
a=df.style.set_table_styles(
       [{
           'selector': 'th',
           'props': [
               ('background-color', 'black'),
               ('color', 'cyan')]
       }])
#st.table(a,900,400)
st.dataframe(a,900,100)

