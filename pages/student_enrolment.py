import streamlit as st
st.title("Daniel School Student Enrolment Page")
subjects=st.multiselect("Select Subjects for Enrolment",["Mathematics","Science","History","Art","Physical Education","Computer Science","Literature"])
st.write("You have selected the following subjects for enrolment:")
for subject in subjects:
    st.write("- " + subject)    