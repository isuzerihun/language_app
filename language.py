from transformers import pipeline
import streamlit as st

st.header("AI Translator: Let AI Remove Your Language Barriers")

col1, col2 = st.columns([1, 1])

model_options = {
    "French to English": "Helsinki-NLP/opus-mt-fr-en",
    "English to French": "Helsinki-NLP/opus-mt-en-fr",
    "Spanish to English": "Helsinki-NLP/opus-mt-es-en",
    "English to Spanish": "Helsinki-NLP/opus-mt-en-es",
    "Italian to English": "Helsinki-NLP/opus-mt-it-en",
    "English to Italian": "Helsinki-NLP/opus-mt-en-it",
    "English to German": "Helsinki-NLP/opus-mt-en-de",
    "German to English": "Helsinki-NLP/opus-mt-de-en",
}

with col1:
    option_llm = st.selectbox("Model", list(model_options.keys()))

selected_model = model_options[option_llm]


def get_query():
    input_text = st.text_area(
        label="Your input text",
        key="question_text"
    )
    return input_text


query = get_query()

if st.button("Translate") and query:
    try:
        with st.spinner("Translating..."):
            translator = pipeline("translation", model=selected_model)
            output = translator(query)[0]["translation_text"]
    except Exception as e:
        output = f"Sorry: cannot translate! {e}"
    

    st.text_area("Response", value=output, height=100)
