import streamlit
# Import pandas library
import pandas as pd
 
# initialize list of lists
data = [['tom', 10], ['nick', 15], ['juli', 14]]
 
# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age'])
df = df.style.set_properties(**{
    'background-color': 'green',
    'font-size': '20pt',
})
#df.set_table_styles([cell_hover, index_names, headers])
streamlit.dataframe(df)

#streamlit.dataframe(df.style.set_table_styles([cell_hover, index_names, headers]))
