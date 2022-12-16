import snowflake.connector
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)

st.title("Auto Filter Dataframes in Streamlit")
st.write(
    """This app accomodates the blog [here](<https://blog.streamlit.io/auto-generate-a-dataframe-filtering-ui-in-streamlit-with-filter_dataframe/>)
    and walks you through one example of how the Streamlit
    Data Science Team builds add-on functions to Streamlit.
    """
)  

def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a UI on top of a dataframe to let viewers filter columns

    Args:
        df (pd.DataFrame): Original dataframe

    Returns:
        pd.DataFrame: Filtered dataframe
    """
    modify = st.checkbox("Add filters")

    if not modify:
        return df 
    
    df = df.copy()

    # Try to convert datetimes into a standard format (datetime, no timezone)
    for col in df.columns:
        if is_object_dtype(df['Pipeline Start Time']):
            try:
                df[col] = pd.to_datetime(df['Pipeline Start Time'])
            except Exception:
                pass

        if is_datetime64_any_dtype(df[col]):
            df[col] = df['Pipeline Start Time'].dt.tz_localize(None)
            
    modification_container = st.container()
    with modification_container:
            to_filter_columns = st.multiselect("Filter dataframe on", df.columns)
            for column in to_filter_columns:
                left, right = st.columns((1, 20))
                left.write("↳")
            if is_categorical_dtype(df['Pipeline Status']) or df['Pipeline Executor'].nunique() < 10:
                user_cat_input = right.multiselect(
                    f"Values for {column}",
                    df['Pipeline Status'].unique(),
                    default=list(df['Pipeline Status'].unique()),
                )
                df = df[df['Pipeline Status'].isin(user_cat_input)]

            else:
                user_text_input = right.text_input(f"Substring or regex in {column}",
                                                  )
                if user_text_input:
                    df = df[df[column].astype(str).str.contains(user_text_input)]
    return df

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor() 
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT PIPELINE_NAME,PIPELINE_EXECUTOR,PIPELINE_STATUS,PIPELINE_START_TIME,PIPELINE_END_TIME,PIPELINE_EXECUTION_TIME,CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION,ERROR_DETAILS FROM SNOWVIEW_AUDIT_VW")
res = my_cur.fetchall()
df= pd.DataFrame(res, columns=['Pipeline Name','Pipeline Executor','Pipeline Status','Pipeline Start Time','Pipeline End Time','Pipeline Execution Time','Credits Consumed','Error Details'])
    


st.dataframe(filter_dataframe(df))
