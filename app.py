import streamlit as st
from gpt_module import get_gpt_clarification

st.set_page_config("Medical Bot", layout="centered")

st.title("🤖 Multilingual Medical Assistant")
st.markdown("Ask a health question in your language. The bot will help clarify your symptoms.")

lang = st.selectbox("🌐 Choose Language", ["en", "hi", "es", "fr", "de"], format_func=lambda x: {
    "en": "English", "hi": "Hindi", "es": "Spanish", "fr": "French", "de": "German"
}[x])

user_input = st.text_area("🩺 Describe your symptoms:")

if st.button("💬 Ask Bot"):
    if user_input.strip():
        with st.spinner("Thinking..."):
            reply = get_gpt_clarification(user_input, lang)
            st.success("🧠 Bot's Response:")
            st.write(reply)
    else:
        st.warning("Please enter a question.")
