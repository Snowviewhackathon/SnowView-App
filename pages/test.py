import streamlit
# Import pandas library
import pandas as pd
 
# initialize list of lists
data = [['tom', 10], ['nick', 15], ['juli', 14]]
 
# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age'])
s=df.style.set_table_styles([
                            {
                               "selector":"thead",
                                "props":"font-weight:bold; color:#FF0000; background-color:White; border:1.3px solid black;"
                            },
                            {
                               "selector":"td",
                                "props":"font-size:20px"
                            },
                          
                            {
                               "selector":"stTable",
                                "props":"width:100%;"
                            },

                       ])

#df.set_table_styles([cell_hover, index_names, headers])
streamlit.dataframe(s)

#streamlit.dataframe(df.style.set_table_styles([cell_hover, index_names, headers]))
