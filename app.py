
import streamlit as st
import requests

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
        "Translate from", list(languages.keys()), index=0
    )

with col2:
    target_language = st.selectbox(
        "Translate to", list(languages.keys()), index=1
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
                response = requests.get(
                    "https://api.mymemory.translated.net/get",
                    params={
                        "q": text_input,
                        "langpair": (
                            f"{languages[source_language]}|"
                            f"{languages[target_language]}"
                        )
                    },
                    timeout=30
                )

                response.raise_for_status()
                data = response.json()

                if data.get("responseStatus") != 200:
                    raise ValueError(
                        data.get("responseDetails", "Translation failed.")
                    )

                translated_text = data.get(
                    "responseData", {}
                ).get("translatedText", "")

                if not translated_text:
                    raise ValueError("No translation was returned.")

            st.subheader("Translated Text")
            st.text_area(
                "Translation result",
                value=translated_text,
                height=150
            )
            st.success("Translation completed successfully!")

        except Exception as error:
            st.error("Translation failed. Please try again.")
            st.caption(f"Details: {error}")
