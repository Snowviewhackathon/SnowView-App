import streamlit as st
# Import pandas library
import pandas as pd
import numpy as np
import streamlit as st
from SnowView import check_password

if check_password():
    
    def color_negative(v, color):
        return f"color: {color};" if v < 0 else None
    df = pd.DataFrame(np.random.randn(5, 2), columns=["A", "B"])
    #a=df.style.applymap(color_negative, color='red')  
    #b=df.style.applymap(color_negative, color='red', subset="A")

    #c=df.style.applymap(color_negative, color='red', subset=["A", "B"])

    #d=df.style.applymap(color_negative, color='red',subset=([0,1,2], slice(None)))  
    #e=df.style.applymap(color_negative, color='red', subset=(slice(0,5,2), "A"))

    cell_hover = {  # for row hover use <tr> instead of <td>
        'selector': 'td:hover',
        'props': [('background-color', '#ffffb3')]
    }
    index_names = {
        'selector': '.index_name',
        'props': 'font-style: italic; color: darkgrey; font-weight:normal;'
    }
    headers = {
        'selector': 'th:not(.index_name)',
        'props': 'background-color: #000066; color: white;'
    }
    #a=df.set_table_styles([cell_hover, index_names, headers])

    f=df.style.set_table_styles(
        [{'selector': 'tr:hover',
          'props': [('background-color', 'yellow')]}]
    )  

    g= df.style.set_table_styles({
         'A': [{'selector': '',
               'props': [('color', 'red')]}],
         'B': [{'selector': 'td',
               'props': 'color: blue;'}]
    }, overwrite=False)   

    st.table(g)
    st.dataframe(g)
    #st.dataframe(filter_dataframe(df.style.set_properties(**{'font-size':'24pt'}))                                                   


