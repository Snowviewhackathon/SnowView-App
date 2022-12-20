import streamlit as st
# Import pandas library
import pandas as pd

data = [['tom', 10], ['nick', 15], ['juli', 14]]
 
# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age'])

th_props = [
  ('font-size', '14px'),
  ('text-align', 'center'),
  ('font-weight', 'bold'),
  ('color', '#6d6d6d'),
  ('background-color', '#f7ffff')
  ]
                               
td_props = [
  ('font-size', '12px')
  ]
                                 
styles = [
  dict(selector="th", props=th_props),
  dict(selector="td", props=td_props)
  ]

# table
df2=df.style.set_properties(**{'text-align': 'left'}).set_table_styles(styles)
st.dataframe(df2)


#st.dataframe(filter_dataframe(df.style.set_properties(**{'font-size':'24pt'}))                                                   


