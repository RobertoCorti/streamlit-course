import streamlit as st
from PIL import Image

# display image
img = Image.open("./module_1/data/image_03.jpg")

st.image(img,
         caption="Image",
         use_column_width=True)

# from URL
url = "https://i.pinimg.com/originals/cb/3c/3d/cb3c3d0d4eab565d6aa0bc185ca8ae94.jpg"
st.image(url,
         caption="Image from URL",
         use_column_width=True)

# display video
video_file = open("./module_1/data/secret_of_success.mp4", "rb").read()
st.video(video_file)

# audio
audio_file = open("./module_1/data/song.mp3", "rb")
st.audio(audio_file.read(), format="audio/mp3")
