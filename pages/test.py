import streamlit as st
# Import pandas library
import pandas as pd
import numpy as np

def color_negative(v, color):
    return f"color: {color};" if v < 0 else None
df = pd.DataFrame(np.random.randn(5, 2), columns=["A", "B"])
#a=df.style.applymap(color_negative, color='red')  
b=df.style.applymap(color_negative, color='red', subset="A")
 
c=df.style.applymap(color_negative, color='red', subset=["A", "B"])
  


st.dataframe(c)
#st.dataframe(filter_dataframe(df.style.set_properties(**{'font-size':'24pt'}))                                                   


