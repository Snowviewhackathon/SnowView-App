import streamlit


streamlit.sidebar.markdown("# Main page 🎈")

streamlit.markdown(f'<h1 style="color:#1874CD;font-size:40px;">{"Snow View"}</h1>', unsafe_allow_html=True)
streamlit.markdown(f'<h1 style="color:#6495ED;font-size:24px;">{"Snowflake Process : Execution Details"}</h1>', unsafe_allow_html=True)

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
    streamlit.markdown(
         f"""
         <style>
         .stApp {{
             #background: url("");
             background-color: black;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    
set_bg_hack_url() 
