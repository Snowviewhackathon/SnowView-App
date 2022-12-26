import snowflake.connector
import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
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
        df1=df.head(15)
        return df1 
    
    df = df.copy()

    # Try to convert datetimes into a standard format (datetime, no timezone)
    for col in df.columns:
        if is_object_dtype(df[col]):
            try:
                df[col] = pd.to_datetime(df[col])
            except Exception:
                pass

        if is_datetime64_any_dtype(df[col]):
            df[col] = df[col].dt.tz_localize(None)
            
    modification_container = st.container()
    with modification_container:
            to_filter_columns = st.multiselect("Filter dataframe on", df.columns)
            for column in to_filter_columns:
                left, right = st.columns((1, 20))
                left.write("↳")
               
                if is_categorical_dtype(df[column]) or df[column].nunique() < 10:
                    user_cat_input = right.multiselect(
                        f"Values for {column}",
                        df[column].unique(),
                        default=list(df[column].unique()),
                    )
                    df = df[df[column].isin(user_cat_input)]
                elif is_numeric_dtype(df[column]):
                    _min = float(df[column].min())
                    _max = float(df[column].max())
                    step = (_max - _min) / 100
                    user_num_input = right.slider(
                        f"Values for {column}",
                        min_value=_min,
                        max_value=_max,
                        value=(_min, _max),
                        step=step,
                    )
                    df = df[df[column].between(*user_num_input)]
                elif is_datetime64_any_dtype(df[column]):
                    user_date_input = right.date_input(
                        f"Values for {column}",
                        value=(
                            df[column].min(),
                            df[column].max(),
                        ),
                    )
                    if len(user_date_input) == 2:
                        user_date_input = tuple(map(pd.to_datetime, user_date_input))
                        start_date, end_date = user_date_input
                        df = df.loc[df[column].between(start_date, end_date)]
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
df= pd.DataFrame(res, columns=['Pipeline Name','Pipeline Executor','Pipeline Status','Pipeline Start Time','Pipeline End Time','Pipeline Execution Time (in seconds)','Credits Consumed','Error Details'])
st.markdown(f'<h1 style="color:#FFFFFF;font-size:48px;">{"❄️SnowView"}</h1>', unsafe_allow_html=True)
#st.markdown(f'<h1 style="color:#FFFFFF;font-size:24px;text-align: center;">{"Historical Usage Metrics"}</h1>', unsafe_allow_html=True)   
st.markdown(
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
#st.dataframe(filter_dataframe(df))
#st.dataframe(df)
#st.line_chart(df, x='Pipeline Start Time', y='Credits Consumed')
st.line_chart(df)
