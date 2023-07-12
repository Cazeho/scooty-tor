import streamlit as st


st.set_page_config(page_title="home",  page_icon="🧭")
st.sidebar.header("Home")

st.title("Scooty-Tor")


search=st.text_input("Search a website in the Dark Web")

if q is not None:
    st.write(search)
