import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


#@st.cache
def load_data():
    """Load the iris dataset."""
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    return df, iris.target_names

df, iris_target_name = load_data()

model = RandomForestClassifier()
model.fit(df.iloc[:,:-1], df['target'])

st.title("Iris Flower Classification")
sepal_length = st.sidebar.slider("Sepal length", float (df['sepal length (cm)'].min()), float (df['sepal length (cm)'].max()))
sepal_width = st.sidebar.slider("Sepal width", float(df ['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))
petal_length = st.sidebar.slider("Petal length", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))
petal_width = st.sidebar.slider("Petal width", float (df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))

input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

# Predict the class
prediction = model.predict(input_data)  
predicted_species = iris_target_name[prediction[0]]
st.write(f"Predicted species: {predicted_species}")