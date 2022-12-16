import streamlit as st
import pandas as pd
'''
def dataframe():
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_cur = my_cnx.cursor() 
    my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
    my_cur.execute("SELECT PIPELINE_NAME,PIPELINE_EXECUTOR,PIPELINE_STATUS,PIPELINE_START_TIME,PIPELINE_END_TIME,PIPELINE_EXECUTION_TIME,CREDITS_CONSUMED_FOR_PIPELINE_EXECUTION,ERROR_DETAILS FROM SNOWVIEW_AUDIT_VW")
    res = my_cur.fetchall()
    df= pd.DataFrame(res, columns=['Pipeline Name','Pipeline Executor','Pipeline Status','Pipeline Start Time','Pipeline End Time','Pipeline Execution Time','Credits Consumed','Error Details'])
    
    return df'''


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
