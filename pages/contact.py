import streamlit as st
from funcs import send_email
from email.message import EmailMessage
st.title("CONTACT")
st.divider()

st.subheader("Această aplicație a fost creată de către Capătă Ciprian."
             "Pentru mai multe informații mă puteți contacta la:")

st.markdown("#")

st.text("Phone: +40075 870 5895")
st.text("Gmail: cipriangheorghecapata@gmail.com")

st.markdown("#")

st.subheader("Sau prin completarea următorului formular:")
with st.form(key='emails_form'):
    user_email = st.text_input("Email")
    raw_message = st.text_area("Mesaj")

    button = st.form_submit_button("Trimite")
    if button:
        if user_email and raw_message:
            send_email(user_email, message_raw=raw_message, gmail_pass=st.secrets["gmail-api-pass"])
            st.success("Email-ul a fost trimis cu succes!",icon="✅")
        else:
            st.error("Completa-ți câmpurile necesare!", icon="🚨")