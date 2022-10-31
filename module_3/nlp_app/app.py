import pandas as pd
import streamlit as st
import streamlit.components.v1 as stc

import spacy
import neattext as nt
import neattext.functions as nfx
from spacy import displacy
from collections import Counter

from textblob import TextBlob

nlp = spacy.load("en_core_web_sm")


def text_analyzer(text):
    docx = nlp(text)
    allData = [(token.text, token.shape_, token.pos_, token.tag_, token.lemma_, token.is_alpha, token.is_stop) for token
               in docx]
    df = pd.DataFrame(allData, columns=["Token", "Shape", "POS", "Tag", "Lemma", "Is_Alpha", "Is_Stopword"])
    return df


def get_entities(text):
    docx = nlp(text)
    entities = [(entity.text, entity.label_) for entity in docx.ents]
    return entities


HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""


# @st.cache
def render_entities(rawtext):
    docx = nlp(rawtext)
    html = displacy.render(docx, style="ent")
    html = html.replace("\n\n", "\n")
    result = HTML_WRAPPER.format(html)
    return result


def get_most_common_tokens(text, num=4):
    word_tokens = Counter(text.split())
    most_common_tokens = dict(word_tokens.most_common(num))
    return most_common_tokens


def get_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return sentiment


def main():
    st.title("NLP App with Streamlit")
    menu = ["Home", "NLP(files)", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home: Analyze text")
        raw_text = st.text_area("Your Text", "Type Here")
        num_of_most_common = int(st.sidebar.number_input("Number of most common tokens", 5, 15))
        if st.button("Analyze"):
            with st.expander("Original Text"):
                st.write(raw_text)

            with st.expander("Text Analysis"):
                token_result_df = text_analyzer(raw_text)
                st.dataframe(token_result_df)

            with st.expander("Entities"):
                stc.html(render_entities(raw_text), height=1000, scrolling=True)

            col1, col2 = st.columns(2)

            with col1:
                with st.expander("Word stats"):
                    st.info("Word Stats")
                    docx = nt.TextFrame(raw_text)
                    st.write(docx.word_stats())

                with st.expander("Top keywords"):
                    st.info("Top keywords/tokens")
                    keywords = get_most_common_tokens(raw_text, num_of_most_common)
                    st.write(keywords)
                with st.expander("Sentiment"):
                    sentiment_result = get_sentiment(raw_text)
                    st.write(sentiment_result)
            with col2:
                with st.expander("Plot Word Frequency"):
                    pass
                with st.expander("Plot Part of Speech"):
                    pass
                with st.expander("Plot Word Cloud"):
                    pass

            with st.expander("Download Text Analysis Results"):
                pass

    elif choice == "NLP(files)":
        st.subheader("NLP Task")
    else:
        st.subheader("About")


if __name__ == "__main__":
    main()
