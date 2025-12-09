import streamlit as st



st.set_page_config(
     page_title = ' Multiple App'
)
st.title('Success Tech World and Accessleration')

st.subheader('We Offer The Best Tech and Accessoiest')

col1, col2, col3 = st.columns(3)

with col1:
    st.caption('Logos')
    st.image('./images/1.jpeg')
    st.button('Click Me', key='btn1')

with col2:
    st.caption('Logos STWA')
    st.image('./images/2.jpeg')
    st.button('Click Me', key='btn2')
