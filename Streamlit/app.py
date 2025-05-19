import streamlit as st
import pandas as pd
import numpy as np

## title of application
st.title("Hello Streamlit")

##display 
st.write("This is a simple Streamlit application.")

## create a dataframe
df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4, 5],
    'Column 2': ['A', 'B', 'C', 'D', 'E'],
})

## display the dataframe
st.write("Here is a sample dataframe:")
st.dataframe(df)

##create a line chart
st.write("Here is a line chart:")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)
