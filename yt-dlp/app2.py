import streamlit as st
import yt_dlp

url = st.text_input("URL YouTube")

if st.button("Télécharger"):
    ydl_opts = {
        "outtmpl": "video.%(ext)s",
        "quiet": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    st.success("Téléchargement terminé")
