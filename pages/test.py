import streamlit as st
# Import pandas library
import pandas as pd
import seaborn as sns
 
# initialize list of lists
data = [['tom', 10], ['nick', 15], ['juli', 14]]
 
# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age'])


 
# Declaring the cm variable by the
# color palette from seaborn
cm = sns.light_palette("green", as_cmap=True)
 
# Visualizing the DataFrame with set precision
print("\nModified Stlying DataFrame:")
#df.style.background_gradient(cmap=cm).set_precision(2)

 
#st.dataframe(filter_dataframe(df.style.set_properties(**{'font-size':'24pt'})))
st.dataframe(dfdf.style.background_gradient(cmap=cm).set_precision(2))                                                       


