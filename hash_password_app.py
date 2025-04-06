# hash_password_app.py

import streamlit as st
import streamlit_authenticator as stauth

st.set_page_config(page_title="Password Hasher", page_icon="🔐")

st.title("🔐 CineScope Password Hasher")
st.markdown("Use this tool to hash a password for `config.yaml`.")

password = st.text_input("Enter Password to Hash", type="password")

if st.button("Generate Hash"):
    if password:
        hashed_pw = stauth.Hasher([password]).generate()[0]
        st.success("✅ Hashed Password:")
        st.code(hashed_pw, language='yaml')
        st.info("🔁 Copy the above hash into your config.yaml file.")
    else:
        st.warning("⚠️ Please enter a password first.")
