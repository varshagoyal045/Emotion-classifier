import streamlit as st

# EDA packages

import pandas as pd
import numpy as np
import altair as alt

import joblib

pipe_lr = joblib.load(open("models\emotion_classifier_pipe_lr_08_2023.pkl", "rb"))

def perdict_emtions(docs):
    results = pipe_lr.predict([docs])
    return results

def get_prediction_proba(docs):
     results = pipe_lr.predict_proba([docs])
     return results


def main():
    st.title("emotion classifier app")
    menu = ["Home" , "Monitor" , "About"]
    chioce = st.sidebar.selectbox("Menu" , menu)

    if chioce=="Home":
        st.subheader("home editor in text")

        with st.form(key='emotion_clf_form'):
            raw_text = st.text_area('Type Here')
            submit_text = st.form_submit_button(label="Submit")

        

        if submit_text:
            col1,col2 = st.columns(2)

            prediction = perdict_emtions(raw_text)
            probability = get_prediction_proba(raw_text)

            with col1:
                st.success("original text")
                st.write(raw_text)

                st.success("prediction")
                st.write(prediction)

            
            with col2:
                st.success("prediction probability")
                st.write(probability)
                proba_df = pd.DataFrame(probability , columns=pipe_lr.classes_)
                # st.write(proba_df.T)
                proba_df_clean = proba_df.T.reset_index()
                proba_df_clean.columns = ["emotions" , "probability"]

                fig = alt.Chart(proba_df_clean).mark_bar().encode(x='emotions' , y='probability')
                st.altair_chart(fig , use_container_width=True)

    elif chioce == "Monitor":
        st.subheader("Monitor page")
    
    else:
        st.subheader("About")


if __name__ == '__main__':
    main()




