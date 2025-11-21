import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("Daniel School Subject wise Student Marks")
st.write("Bar Chart for different subject Marks:")
data={'subjects':['Maths','Science','English','Social Studies','Hindi'],
      'marks':[88,92,85,90,87]}
df=pd.DataFrame(data)
st.subheader("Bar Chart of Subject wise Marks") 
d=df.set_index('subjects')
st.bar_chart(d)
