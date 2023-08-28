import streamlit as st

# summary packages

# from gensim.summarization import summarize


from collections.abc import Mapping
from collections.abc import MutableMapping
from collections.abc import Sequence

# sumy pkgs
from sumy.parsers.plaintext import PlainTextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

# function for sumy summarization

def sumy_summarizer(docs):
    parser = PlainTextParser.from_string(docs ,Tokenizer("english"))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document , 3)
    summary_list = [str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    return result


def main():

    st.title("Summarizer and entity checker")

    activity = ["Summarize" , "Entity-Checker"]

    choice = st.selectbox("select activity" , activity)

    if choice=="Summarize":
        st.subheader("Summary with NLP")
        raw_text = st.text_area("Enter your text here" , "Type here")

        summary_choice = st.selectbox("Summary type" , ["Gensim" , "Sumy Lex Rank"])

        if st.button("Summarize"):
            if summary_choice == "Sumy Lex Rank":
                summary_result = sumy_summarizer(raw_text)
 

            # if summary_choice =="Gensim":
            #     summary_result = summarize(raw_text)
            # el
               
    st.write(summary_result)




if __name__== "__main__":
    main()