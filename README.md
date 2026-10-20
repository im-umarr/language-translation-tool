# 🌍 Language Translation Tool

A simple and interactive language translation application built with Python and Streamlit. It allows users to translate text between multiple languages using the MyMemory Translation API.

## ✨ Features

- Translate text between multiple languages.
- Supports English, Urdu, Hindi, Arabic, French, Spanish, German, Italian, Chinese, Japanese, Korean, Portuguese, Russian, and Turkish.
- Simple and user-friendly interface.
- Source and target language selection.
- Input validation for empty text and identical languages.
- Loading indicator while translating.
- Error handling for failed requests.
- Supports text input up to 5,000 characters.

## 🛠️ Technologies Used

- Python
- Streamlit
- Requests
- MyMemory Translation API

## 📁 Project Structure

```text
language-translation-tool/
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/im-umarr/language-translation-tool.git
```

### 2. Open the project folder

```bash
cd language-translation-tool
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m streamlit run app.py
```

The application will open in your browser. If it does not open automatically, visit:

`http://localhost:8501`

## 🚀 How to Use

1. Select the source language.
2. Select the target language.
3. Enter the text you want to translate.
4. Click the **Translate** button.
5. View the translated text in the results section.

## ⚠️ Notes and Limitations

- An active internet connection is required.
- Translation requests depend on the availability and usage limits of the MyMemory API.
- Translation quality and supported language pairs may vary.
- The application does not use a locally trained translation model.

## 🎯 Project Objective

This project was developed as part of an AI internship task to practice Python application development, API integration, input validation, exception handling, and building interactive applications with Streamlit.

## 👨‍💻 Author

**Umar Abid**

GitHub: [im-umarr](https://github.com/im-umarr)

---

*Built with Python and Streamlit.*
