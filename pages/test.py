import streamlit
# Import pandas library
import pandas as pd
 
# initialize list of lists
data = [['tom', 10], ['nick', 15], ['juli', 14]]
 
# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age'])
sp=df.style.set_table_styles([
                            {
                               "selector":"thead",
                                "props":"font-weight:bold; color:#FF0000; background-color:green; border:1.3px solid black;"
                            },
                            {
                               "selector":"td",
                                "props":"font-size:50px"
                            },
                          
                            {
                               "selector":"stTable",
                                "props":"width:100%;"
                            },

                       ])
s=df.style.set_table_styles([
                           {
                               "selector":"thead",
                               "props":"background-color:dodgerblue; color:white; border:3px solid red;"
                           },



                      ])



type(s)

#df.set_table_styles([cell_hover, index_names, headers])
streamlit.dataframe(s)
streamlit.table(s) 

#streamlit.dataframe(df.style.set_table_styles([cell_hover, index_names, headers]))
