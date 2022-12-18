import streamlit
# Import pandas library
import pandas as pd
 
# initialize list of lists
data = [['tom', 10], ['nick', 15], ['juli', 14]]
 
# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age'])

streamlit.dataframe(df.style.set_table_styles({
    'A': [{'selector': '',
           'props': [('color', 'red')]}],
    'B': [{'selector': 'td',
           'props': 'color: blue;'}]
}, overwrite=False))
