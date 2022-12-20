import streamlit as st
# Import pandas library
import pandas as pd

def color_negative(v, color):
    return f"color: {color};" if v < 0 else None
df = pd.DataFrame(np.random.randn(5, 2), columns=["A", "B"])
a=df.style.applymap(color_negative, color='red')  

#st.dataframe(   df.style.applymap(color_negative_red).apply(highlight_max, color="darkorange", axis=0))
st.dataframe(a)
#st.dataframe(filter_dataframe(df.style.set_properties(**{'font-size':'24pt'}))                                                   


