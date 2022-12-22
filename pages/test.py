import streamlit as st
import pandas as pd

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 
st.dataframe(df.style.highlight_max(axis=0, props='background-color:green;', subset=['A','B'])
         .highlight_min(axis=0, props='background-color:red;', subset=['A','B']))
#st.dataframe(df)
