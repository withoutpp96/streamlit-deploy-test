import streamlit as st

st.set_page_config(page_title="Demo", page_icon="🎈", layout="wide")
st.title("Hello, JINSUMMISSI 😄?!")
name = st.text_input("What's Your name?")
st.write(f"Nice to meet you, {name or 'friend'} ❤️")
