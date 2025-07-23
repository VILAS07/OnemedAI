import os
import streamlit as st
from dotenv import load_dotenv
from compare import PdfCompare
from pdf_extractor import extract_text

load_dotenv()

scans = (
    "Document-Level Cosine Similarity Scan",
    "Sentence-Level Cosine Similarity Scan",
    "Preprocessed Sentence-Level Cosine Similarity Scan",
)

st.title("PDF Comparison Tool")

# * PDF Upload
col1, col2 = st.columns(2)
with col1:
    pdf1 = st.file_uploader("1st PDF", type=["pdf"])
with col2:
    pdf2 = st.file_uploader("2nd PDF", type=["pdf"])

# * Scan Type
st.markdown("---")
option = st.radio(
    "Choose type of Scan",
    scans,
    horizontal=True,
    captions=["upto 5mins", "upto 5mins", "upto 5mins"],
    key="scans",
)

if option:
    if option == scans[0]:
        st.subheader(f"{scans[0]}ing")
        st.write(
            "Embeds the entire content of PDFs into vectors using embedding models. Cosine similarity is then calculated to compare the overall semantic content. This is a quick scan and is suitable for comparing large documents."
        )
    elif option == scans[1]:
        st.subheader(f"{scans[1]}ing")
        st.write(
            "Splits PDFs into sentences and embeds each sentence into vectors. The cosine similarity between sentence vectors is computed to assess semantic similarity at the sentence level. This is a moderate scan and is suitable for comparing documents with multiple sections or paragraphs."
        )
    elif option == scans[2]:
        st.subheader(f"{scans[2]}ing")
        st.write(
            "Splits PDFs into sentences, preprocesses them (cleaning, stemming), then embeds the cleaned sentences into vectors. Cosine similarity is used to compare the semantic content of the preprocessed sentences. This is a thorough scan and is suitable for comparing documents with complex or technical content."
        )

    # * Embedding Type
    vector = st.radio(
        "Choose Embedding Type:",
        ("Count Vectorizer", "TF-IDF Vectorizer", "all-MiniLM-L6-v2"),
        index=0,
        horizontal=True,
        captions=["", "", "Method with Longer Processing Time"],
        key="vector",
    )

# * Submit button
if st.button("Submit"):
    with st.spinner("Comparing PDFs..."):
        embed = (
            0
            if vector == "Count Vectorizer"
            else 1 if vector == "TF-IDF Vectorizer" else 2
        )
        if pdf1 and pdf2:
            text1 = extract_text(pdf1)
            text2 = extract_text(pdf2)

            pdf_compare = PdfCompare(text1, text2)
            if option == scans[0]:
                similarity = pdf_compare.quick_scan(embed)
            elif option == scans[1]:
                similarity = pdf_compare.moderate_scan(embed)
            elif option == scans[2]:
                similarity = pdf_compare.thorough_scan(embed)
            
            if similarity > 0.5:
                st.success("The PDFs are similar.")
            else:
                st.error("The PDFs are not similar.")
            st.progress(int(similarity * 100))
            st.title(f"Similarity Score: {similarity:.2f}")
        else:
            st.error("Please upload PDFs to compare.")
