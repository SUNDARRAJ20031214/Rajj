import streamlit as st
st.title("Hotel Sales App")
tab1,tab2=st.tabs(["Tab1","Tab2"])
with tab1:
  st.subheader("Home")
with tab2:
  st.subheader("About Us")
