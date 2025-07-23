import streamlit as st
from report_comparator import ReportComparator
import os

def main():
    st.set_page_config(
        page_title="AI Radiology Report Comparator",
        page_icon="🏥",
        layout="wide"
    )
    
    st.title("AI-Based Radiology Report Comparator")
    st.markdown("""
    This tool compares AI-generated radiology reports with original (radiologist-written) reports 
    to identify significant differences. Upload both reports to begin the analysis.
    """)
    
    # Model selection
    model = st.sidebar.selectbox(
        "Select Ollama Model",
        ["llama3:latest", "mistral", "llama2", "phi", "gemma"],
        index=0
    )
    
    # File uploaders
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Original Report (Human)")
        original_file = st.file_uploader("Upload original radiology report", type=["pdf", "png", "jpg", "jpeg", "bmp", "tiff", "tif"])
    
    with col2:
        st.subheader("AI-Generated Report")
        ai_file = st.file_uploader("Upload AI-generated report", type=["pdf", "png", "jpg", "jpeg", "bmp", "tiff", "tif"])
    
    # Question input
    question = st.text_area("Ask a specific question about the reports (optional):", height=100)
    
    # Compare button
    if original_file and ai_file:
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Compare Reports"):
                with st.spinner("Analyzing reports..."):
                    try:
                        # Initialize comparator with selected model
                        comparator = ReportComparator(model=model)
                        
                        # Compare reports
                        result = comparator.compare(original_file, ai_file)
                        
                        # Display results
                        st.success("Analysis complete!")
                        
                        # Display side-by-side comparison
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.subheader("Original Report")
                            st.text_area("Text", result["original_text"], height=400, key="original_text_area")
                        
                        with col2:
                            st.subheader("AI-Generated Report")
                            st.text_area("Text", result["ai_text"], height=400, key="ai_text_area")
                        
                        # Display differences
                        st.subheader("Significant Differences")
                        st.markdown(result["comparison"])
                        
                    except Exception as e:
                        st.error(f"An error occurred: {str(e)}")
        
        with col2:
            if question and st.button("Ask Question"):
                with st.spinner("Processing question..."):
                    try:
                        # Initialize comparator with selected model
                        comparator = ReportComparator(model=model)
                        
                        # Ask the question
                        answer = comparator.ask_question(original_file, ai_file, question)
                        
                        # Display answer
                        st.success("Question answered!")
                        st.subheader("Answer")
                        st.markdown(answer)
                        
                    except Exception as e:
                        st.error(f"An error occurred: {str(e)}")
    else:
        st.info("Please upload both reports to begin comparison.")
    
    # Add information about the project
    st.sidebar.markdown("## About")
    st.sidebar.markdown("""
    This tool uses:
    - **PyPDF2** for PDF text extraction
    - **Tesseract OCR** for image text extraction
    - **Ollama** for local LLM analysis
    - **Streamlit** for the user interface
    
    Ensure Ollama is running locally with your selected model.
    """)

if __name__ == "__main__":
    main()