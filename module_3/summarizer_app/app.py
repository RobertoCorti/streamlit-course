import streamlit as st

from gensim.summarization.summarizer import summarize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

import pandas as pd


def sumy_summarizer(docx, num=2):
    """
    Summarize text using sumy

    Parameters
    ----------

    docx : str
        The text to summarize
    num : int
        The number of sentences to return

    Returns
    -------

    summary : str
        The summary of the text
    """
    parser = PlaintextParser.from_string(docx, Tokenizer("english"))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document, num)
    summary_list = [str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    return result


def main():
    """
    A simple summarization NLP app
    """
    st.title("Summarization App")
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Summarization")
        raw_text = st.text_area("Enter Text Here")
        if st.button("Summarize"):
            with st.expander("Original Text"):
                st.write(raw_text)

            c1, c2 = st.columns(2)

            with c1:
                with st.expander("LexRank Summary"):
                    my_summary = sumy_summarizer(raw_text)
                    st.write(my_summary)

            with c2:
                with st.expander("Gensim Summary"):
                    my_summary = summarize(raw_text)
                    st.write(my_summary)
    else:
        st.subheader("About")


if __name__ == "__main__":
    main()
