import streamlit as st
from pytubefix import YouTube
from pytubefix.cli import on_progress

st.title("Hello world")

url = st.text_input("Copiez-coller le lien de la vidéo", "https://www.youtube.com")

if st.button("Télécharger MP4", type="primary"):
    yt = YouTube(url, on_progress_callback=on_progress)
    st.write("Téléchargement de :", {yt.title})
    ys = yt.streams.get_highest_resolution()
    ys.download(output_path="files")

if st.button("Télécharger son uniquement", type="secondary"):
    yt = YouTube(url, on_progress_callback=on_progress)
    ys = yt.streams.get_audio_only()
    ys.download(output_path="files")
