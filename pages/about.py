import streamlit as st 

st.title('This is my page')

with st.form(' user form'):
    username = st.text_input(' Enter Username')
    password = st.text_input('Enter Password')
    submitted = st.form_submit_button('submit')