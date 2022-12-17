import streamlit

modification_container = streamlit.container()
with modification_container:
    streamlit.markdown("<h1 style='text-align: center; color: white;font-size:80px'>❄️Snow View❄️</h1>", unsafe_allow_html=True)
    streamlit.markdown(
        f"""
        <style>
        section[data-testid="stSidebar"] > div:first-of-type {
        background-color: var(--secondary-background-color);
        width: 250px;
        padding: 4rem 0;
        box-shadow: -2rem 0px 2rem 2rem rgba(0,0,0,0.16);
        }
		</style>
		""",
		unsafe_allow_html=True
     )
    
