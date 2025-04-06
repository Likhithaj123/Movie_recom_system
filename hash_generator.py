import streamlit_authenticator as stauth

passwords = ['likhithaj123']
hashed = stauth.Hasher(passwords).generate()

print(hashed)
