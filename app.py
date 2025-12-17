import streamlit as st
from pytubefix import YouTube
from pytubefix.cli import on_progress

st.title("Téléchargement depuis YouTube")

url = st.text_input("Copiez-coller le lien de la vidéo", "https://www.youtube.com/watch?v=iyLdoQGBchQ")

if url:
    yt = YouTube(url, on_progress_callback=on_progress)
    st.text(yt.title)
    st.video(url)

    if st.button("Télécharger MP4", type="primary"):
        st.write("Téléchargement de :", yt.title)
        ys = yt.streams.get_highest_resolution()
        ys.download(output_path="files/")
        st.success("Téléchargement terminé !")

    if st.button("Télécharger son uniquement", type="secondary"):
        ys = yt.streams.get_audio_only()
        ys.download(output_path="files/")
        st.success("Téléchargement terminé !")
else:
    st.markdown(":orange-badge[⚠️ Entrer un lien ci-dessus]")
