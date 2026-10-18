
import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 Language Translation Tool")
st.write("Translate text between different languages.")

languages = {
    "English": "en",
    "Urdu": "ur",
    "Hindi": "hi",
    "Arabic": "ar",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Chinese (Simplified)": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Portuguese": "pt",
    "Russian": "ru",
    "Turkish": "tr"
}

col1, col2 = st.columns(2)

with col1:
    source_language = st.selectbox(
        "Translate from",
        list(languages.keys()),
        index=0
    )

with col2:
    target_language = st.selectbox(
        "Translate to",
        list(languages.keys()),
        index=1
    )

text_input = st.text_area(
    "Enter text to translate",
    placeholder="Type your text here...",
    height=150,
    max_chars=5000
)

if st.button("Translate", type="primary", use_container_width=True):
    if not text_input.strip():
        st.warning("Please enter some text first.")

    elif source_language == target_language:
        st.warning("Please select two different languages.")

    else:
        try:
            with st.spinner("Translating your text..."):
                translator = GoogleTranslator(
                    source=languages[source_language],
                    target=languages[target_language]
                )
                translated_text = translator.translate(text_input)

            st.subheader("Translated Text")
            st.text_area(
                "Translation result",
                value=translated_text or "",
                height=150
            )

            if translated_text:
                st.success("Translation completed successfully!")

        except Exception as error:
            st.error(
                "Translation failed. Please check your internet "
                "connection and try again."
            )
            st.caption(f"Technical details: {error}")
