import streamlit

modification_container = streamlit.container()
with modification_container:
    streamlit.markdown("<h1 style='text-align: center; color: white;font-size:80px'>❄️Snow View❄️</h1>", unsafe_allow_html=True)
    streamlit.markdown(
     f"""
     <style>
     .stApp {{
         #background: url("");
         background-color: #86b6fd;
         #background-size: cover
     }}
     </style>
     """,
     unsafe_allow_html=True
    )
