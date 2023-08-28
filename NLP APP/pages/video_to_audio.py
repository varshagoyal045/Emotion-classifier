import moviepy.editor

import streamlit as st

st.header("Video to Audio Converter")
st.write("extract audio from video")

def converter(video_file):
    video = moviepy.editor.VideoFileClip(video_file)
    audio = video.audio
    audio.write_audiofile("Audio.mp3")
    return audio
    

def main():
    video_input = st.file_uploader("Upload your Video here" , type=['mp4' , 'WMV' , 'AVI'])
    if video_input is not None:
       if st.button("Convert"):
           result = converter(video_input)
           audio_bytes = result.read() 
           st.success("Output Audio is : ")
           st.audio(audio_bytes, format='audio/ogg') 



if __name__=="__main__":
    main()






