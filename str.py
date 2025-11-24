import streamlit as st
st.title("Hotel Sales App")
tab1,tab2=st.tabs("tab1","tab2")
with tab1:
  st.subheader("Home")
with tab2:
  st.subheader("About Us")
