import streamlit as st

st.write("Minimal test app")
name = st.text_input("Type something")
if st.button("Click me"):
    st.success(f"Button works. You typed: {name}")
