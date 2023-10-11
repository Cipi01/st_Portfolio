import streamlit as st
from PIL import Image
import pandas as pd

#st.set_page_config(layout='wide')
col1, col2 = st.columns(2)
me_image = Image.open('imgs/eu.jpg')

col1.image(me_image, use_column_width=True)
col2.header("Capătă Ciprian")
col2.info("""Fost ofițer în cadrul Forțelor Terestre ale Armatei Române, cu o experiență limitată dar aprofundată în 
cadrul managementului logisticii și cu o pasiune pentru sectorul IT, în special software. Mă consider o persoană 
pro-activă, ambițioasă în cadrul atât al muncii prestate cât și al proiectelor personale, cu o gândire analitică, 
logică și îndreptată în special înspre partea de automatizare.""")
st.divider()
st.header("Proiecte personale")

col1, col2 = st.columns(2)
df = pd.read_csv("programs.csv")
df_len = int(df.__len__() / 2)
with col1:
    for index, row in df[:df_len].iterrows():
        st.subheader(row['Name'])
        img1 = Image.open(row['ImgPath'])
        st.image(row['ImgPath'])
        st.markdown(f"<h4 style='text-align: justify; color: white;font-size: 16px;'>{row['Desc']} </h4>",
                    unsafe_allow_html=True)
        st.link_button("For code", row['Link'])
with col2:
    for index, row in df[df_len:].iterrows():
        st.subheader(row['Name'])
        st.image(row['ImgPath'])
        st.markdown(f"<h4 style='text-align: justify; color: white;font-size: 16px;'>{row['Desc']} </h4>",
                    unsafe_allow_html=True)
        st.link_button("For code", row['Link'])

st.divider()
st.header("Diplome relevante")
df_cert = pd.read_csv('certifs.csv')

#colX,col1,colY = st.columns(3)
for index, row in df_cert.iterrows():
    st.image(row['ImgPath'])
    col1,col2,col3 = st.columns([1,2,4])
    with col3:
        st.link_button("URL", row['CertfUrl'])
