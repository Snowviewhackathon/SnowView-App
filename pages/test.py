import streamlit
# Import pandas library
import pandas as pd
 
# initialize list of lists
data = [['tom', 10], ['nick', 15], ['juli', 14]]
 
# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age'])
a=df.style.set_table_styles(
    [{'selector': 'tr:hover',
      'props': 'background-color: yellow; font-size: 1em;'}]
)   
streamlit.dataframe(a)
