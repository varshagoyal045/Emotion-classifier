import streamlit as st

from pydub import AudioSegment , silence

audio = st.file_uploader("Upload your audio file" , type = ['mp3' , 'wav'])

if audio:
    audio_segment = AudioSegment.from_file(audio)
    chunks = silence.split_on_silence(audio_segment , min_silence_len=500 , silence_thresh=audio_segment.dBFS-20 , keep_silence=100)
    for chunk in chunks:
        st.write(chunk)
        # print(chunk)
