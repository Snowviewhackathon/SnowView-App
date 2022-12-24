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
st.dataframe(df.style.highlight_max(axis=0, props='background-color:green;', subset=['A','B'])
         .highlight_min(axis=0, props='background-color:red;', subset=['A','B']))
#st.dataframe(df)
authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "SIPL_dashboard", "abcdef")
authenticator.logout("Logout", "sidebar")
