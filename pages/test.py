import streamlit as st
# Import pandas library
import pandas as pd

data = [['tom', 10], ['nick', 15], ['juli', 14]]
 
# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age'])

st.dataframe(df)

st.dataframe(
    df.style.applymap(color_negative_red).apply(
        highlight_max, color="darkorange", axis=0
    )
)
#st.dataframe(df)

#st.dataframe(filter_dataframe(df.style.set_properties(**{'font-size':'24pt'}))                                                   


