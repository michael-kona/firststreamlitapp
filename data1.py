import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("Daniel School Student Performance Analysis")
st.write("Upload a CSV file containing student performance data to visualize and analyze their scores.")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.subheader("Raw Data  Preview ")
    st.write("Data Preview:")
    st.dataframe(data)
    st.write("Line Chart of Student Performance:")
    st.line_chart(data.set_index('Student_Name')[['Marks']])
    st.bar_chart(data.set_index('Student_Name')[['Marks']])
    st.scatter_chart(data.set_index('Student_Name')[['Marks']])