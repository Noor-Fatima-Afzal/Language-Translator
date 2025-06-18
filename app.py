import os
import streamlit as st
from utils.controller import translate_text

# ——————————————————————————————————————————————————————————————————————————
# 1. Page Config & CSS
# ——————————————————————————————————————————————————————————————————————————
st.set_page_config(
    page_title="🌐 Language Translator",
    layout="centered",
    page_icon="🌐"
)

st.markdown("""
<style>
/* Page background */
body { background-color: #f0f2f6; }

/* Header */
h1 { text-align: center; color: #4f46e5; font-size: 2.5rem; margin-bottom: 0.1rem; }
.subtitle { text-align: center; color: #6b7280; font-size: 1.1rem; margin-bottom: 2rem; }

/* Card container */
.card {
  background: #ffffff;
  padding: 2rem;
  margin: 1rem auto;
  border-radius: 0.75rem;
  max-width: 700px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

/* Text areas */
.css-1hynsf2 textarea {
  border-radius: 0.5rem !important;
}

/* Buttons */
.stButton>button {
  background-color: #6366f1 !important;
  color: #ffffff !important;
  border-radius: 0.5rem !important;
  padding: 0.6rem 1.2rem !important;
  font-size: 1rem !important;
  border: none !important;
}
.stButton>button:hover {
  background-color: #4f46e5 !important;
}
</style>
""", unsafe_allow_html=True)

# ——————————————————————————————————————————————————————————————————————————
# 2. Header
# ——————————————————————————————————————————————————————————————————————————
st.markdown("<h1>🌐 Language Translation App</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Instantly translate text between languages using Groq’s AI</p>", unsafe_allow_html=True)

# ——————————————————————————————————————————————————————————————————————————
# 3. Translation Card
# ——————————————————————————————————————————————————————————————————————————
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    
    # Input form
    with st.form(key="translate_form"):
        sentence = st.text_area(
            "📝 Enter text to translate:",
            height=150,
            placeholder="Type or paste your text here..."
        )
        # Language selector
        languages = [
            "French", "Spanish", "German", "Chinese", "Japanese",
            "Russian", "Arabic", "Portuguese", "Hindi", "Other"
        ]
        target_language = st.selectbox("🌍 Target language:", languages)
        if target_language == "Other":
            target_language = st.text_input("Specify language:")
        
        submit = st.form_submit_button("Translate ▶️")
    st.markdown("</div>", unsafe_allow_html=True)

# ——————————————————————————————————————————————————————————————————————————
# 4. Perform Translation & Display
# ——————————————————————————————————————————————————————————————————————————
if submit:
    if sentence.strip() and target_language.strip():
        with st.spinner("Translating…"):
            translation = translate_text(sentence, target_language)
        st.success("✅ Translation Complete!")
        
        # Show result in a second card
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("🚀 Translated Text")
        st.text_area(
            "Result:",
            value=translation,
            height=150
        )
        st.download_button(
            "📥 Download as TXT",
            data=translation,
            file_name="translation.txt",
            mime="text/plain",
            use_container_width=True
        )
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.error("Please enter both the text and the target language.")  
