import streamlit as st

from googletrans import Translator
translator = Translator()

st.header("Text Translation")

def translation(file , destination):
     sent = file.read()
     translated = translator.translate(sent , dest=destination)
     return translated.text

# result = translator.translate(text, dest='hi')
# print(result)
# print(result.src)
# print(result.dest)
# print(result.text)


def main():
    input_type = st.selectbox("choose input language" , ["english" , "hindi" , "punjabi" , "tamil" , "urdu" , "malyalam"])

    uploaded_file = st. file_uploader("Upload your file here...")

    translate_type = st.selectbox("choose destination language" , ["english" , "hindi" , "marathi" , "tamil" , "urdu" , "malyalam"])

    destination = ""

    if translate_type=="english":
        destination = "en"

    elif translate_type=="hindi":
         destination = "hi"
    elif translate_type=="marathi":
         destination = "mr"

    elif translate_type=="tamil":
         destination="ta"
    elif translate_type == "urdu":
         destination = "ur"

    elif translate_type == "malyalam":
         destination = "ml"
    

    if st.button("Translate"):

         output = translation(uploaded_file , destination)
         st.write(output)

if __name__ == "__main__":
     main()


# raw_text = st.text_area

# st.write(uploaded_file)







# if st.button("Translate"):
#     st.write("output")
