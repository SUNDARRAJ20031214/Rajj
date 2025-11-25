import streamlit as st
st.title("Hotel Sales App Logo")
st.markdown("""
    <style>
    .stApp {
        background-color:light blue;     /* Light gray */
    }
    </style>
    """, unsafe_allow_html=True)
tabs=st.tabs(["Home","Menu","About Us","Contact"])
with tabs[0]:
  st.markdown("<h1 style='color:yellow;font-family: Montserrat;'>Raj Restaurant</h1>",unsafe_allow_html=True)
  
  
