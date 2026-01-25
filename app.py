import streamlit as st
from study import extract_text_from_pdf
from generate import generate_questions

st.title("📘 PDF → Quiz Generator")

pdf = st.file_uploader("Upload PDF", type=["pdf"])

if pdf is not None:
    st.success("PDF uploaded!")

    if st.button("Generate Questions"):
        with st.spinner("Reading PDF..."):
            text = extract_text_from_pdf(pdf)

        with st.spinner("Generating Questions..."):
            questions = generate_questions(text)

        st.subheader("Generated Questions:")
        st.write(questions)



