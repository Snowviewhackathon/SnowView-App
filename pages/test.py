import streamlit as st
# Import pandas library
import pandas as pd

def color_negative_red(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    color = "red" #if val < 0 else "black"
    return "color: %s" % color


def highlight_max(data, color="yellow"):
    """highlight the maximum in a Series or DataFrame"""
    attr = "background-color: {}".format(color)
    if data.ndim == 1:  # Series from .apply(axis=0) or axis=1
        is_max = data == data.max()
        return [attr if v else "" for v in is_max]
    else:  # from .apply(axis=None)
        is_max = data == data.max().max()
        return pd.DataFrame(
            np.where(is_max, attr, ""), index=data.index, columns=data.columns
        )

data = [['tom', 10], ['nick', 15], ['juli', 14]]
 
# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age'])

st.dataframe(df.style.format("{:.2%}"))
st.dataframe(df)

st.dataframe(
    df.style.applymap(color_negative_red).apply(
        highlight_max, color="darkorange", axis=0
    )
)
#st.dataframe(df)

#st.dataframe(filter_dataframe(df.style.set_properties(**{'font-size':'24pt'}))                                                   


