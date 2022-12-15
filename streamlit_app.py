import streamlit as st

def main_page():
    #streamlit.sidebar.markdown("# Main page")

#streamlit.markdown(f'<h1 style="color:white;font-size:40px;">{"❄️Snow View❄️"}</h1>', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white;font-size:80px'>❄️Snow View❄️</h1>", unsafe_allow_html=True)

#streamlit.markdown("<h1 style='text-align: center; color: red;'>Some title</h1>", unsafe_allow_html=True)

#streamlit.markdown(f'<h1 style="color:white;font-size:24px;">{"Snowflake Process : Execution Details"}</h1>', unsafe_allow_html=True)

    st.markdown(
         f"""
         <style>
         .stApp {{
             #background: url("");
             background-color: #86b6fd;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    #st.markdown("# Main page")
    #st.sidebar.markdown("# Main page")

def page2():
    st.markdown("# Page 2")
    st.sidebar.markdown("# Page 2")

def page3():
    st.markdown("# Page 3")
    st.sidebar.markdown("# Page 3")

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

