import streamlit as st
from utils import (
    generate_response,
    get_prompt_templates
)

st.set_page_config(page_title="📚 Educational Content Generator", layout="centered")

st.title("📚 Educational Content Generator")
st.markdown("Generate study material tailored to your subject and level.")

content_type = st.selectbox("📌 Select content type", [
    "Lesson Summary", "Quiz Questions", "Concept Explanation", "Flashcards", "Study Tips"
])

subject = st.text_input("📘 Enter the subject or topic")

level = st.selectbox("🎓 Select learner level", ["Beginner", "Intermediate", "Advanced"])

if st.button("🚀 Generate Content"):
    if not subject.strip():
        st.warning("⚠️ Please enter a subject or topic.")
    else:
        prompt = get_prompt_templates(content_type, subject, level)
        st.info(f"🧠 Prompt used:\n\n`{prompt}`")

        with st.spinner("Generating content..."):
            output = generate_response(prompt)

        if output.startswith("⚠️ Error"):
            st.error(output)
        else:
            st.success("✅ Content generated successfully!")
            st.text_area("📄 Generated Content", value=output, height=300)
