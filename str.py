import streamlit as st
st.title("Hotel Sales App Logo")
tabs=st.tabs(["Home","Menu","About Us","Contact"])
with tabs[0]:
  st.markdown("<h1 style='color:green;font-family:"Poppin",sans-serif;'>Raj Restaurant</h1>",unsafe_allow_html=True)
  
