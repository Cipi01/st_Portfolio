import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Web scrapers"
)
col1, x, col2 = st.columns([2, 1, 2])
df = pd.read_csv("webscrapers.csv")
df_len = int(df.__len__() / 2)
with col1:
    for index, row in df[:df_len].iterrows():
        st.subheader(row['Title'])
        st.image(row['LogoImg'])
        st.markdown(f"<h4 style='text-align: justify; color: white;font-size: 16px;'>{row['Desc']} </h4>",
                    unsafe_allow_html=True)
        st.link_button("Pagina GitHub", row['Link'])

with col2:
    for index, row in df[df_len:].iterrows():
        st.subheader(row['Title'])
        st.image(row['LogoImg'])
        st.markdown(f"<h4 style='text-align: justify; color: white;font-size: 16px;'>{row['Desc']} </h4>",
                    unsafe_allow_html=True)
        st.link_button("Pagina GitHub", row['Link'])

st.divider()
st.subheader("Integrare mySQL")
st.markdown(
    f"<h4 style='text-align: justify; color: white;font-size: 16px;'>{'Prin acest program se execută integrarea într-o bază de date mySQL a tuturor datelor preluate prin programele de tip Webscraper.'} </h4>",
    unsafe_allow_html=True)
st.link_button("Pagina Github", "https://github.com/Cipi01/Webscrapers_DB")
