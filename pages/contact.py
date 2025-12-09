import streamlit as st 

st.title('This is my contact page')

with st.form(' user form'):
    name = st.text_input(' Enter Full Name')
    email = st.text_input('Enter Email Address')
    phone = st.number_input('Enter Phone Number')
    select = st.selectbox('Select one',options=['_','Keyboard','Mouse','Joystick','Computer','Iphone','Samsung'])
    message = st.text_area('Write Your Message')
    submitted = st.form_submit_button('Submit')
