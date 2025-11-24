import streamlit as st
st.title("Hotel Sales App Logo")
st.markdown("<h1 style="color=green;">Home</h1>,unsafe_allow_html=True)
tabs=st.tabs(["Home","Menu","About Us","Contact"])
with tabs[0]:
  st.header("Raj Restaurant")
  
