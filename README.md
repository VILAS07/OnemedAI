# 🧠 OnemedAI – AI Radiology Report Comparator

OnemedAI is an advanced AI-powered tool that compares **AI-generated radiology reports** with **radiologist-written reports**, identifies key differences, and enables interactive exploration using local or cloud-based LLM

---

## 🔧 Prerequisites

Before running the app, ensure you have the following installed:

- ✅ Python 3.8 or higher  
- 🧠 [Ollama](https://ollama.com/) – for running LLAMA 3 locally  
- 🔍 [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) – for text extraction from scanned PDFs  

---

## 🚀 Installation & Setup

### 📦 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 🔐 2. Set Up Environment Variables

Create a `.env` file in the root directory and add the following:

```env
GOOGLE_API_KEY=your-google-api-key
DEPLOYED=False
```

### 🤖 3. Set Up LLAMA 3 with Ollama

Download and start LLAMA 3 (8B model):

```bash
ollama run llama3
```

---

## 🧪 Usage

### ▶️ 1. Run the Streamlit App

```bash
streamlit run app.py
```

---

### 🏠 2. Home Page – Report Comparison

Upload and compare two PDF reports:

- 📄 **Upload Reports**: AI vs Radiologist  
- 🧠 **Choose Scan Type**:
  - Document-Level  
  - Sentence-Level  
  - Preprocessed Sentence-Level  
- 🔎 **Select Embedding Method**:
  - Count Vectorizer  
  - TF-IDF Vectorizer  
  - All-MiniLM-L6-v2
- ✅ Click **Submit** to view:
  - Similarity score
  - Highlighted text differences
  - AI interpretation summary

---

### 💬 3. ChatBot Page – Ask Questions to the PDFs

- 📚 Load PDFs into a vector database
- 💡 Choose your LLM (LLAMA 3 or Gemini)
- 🤖 Ask questions related to the content of both PDFs
- 🧩 View interactive responses from the AI

---

## 📁 Project Structure

```
OnemedAI/
├── app.py                     # Main Streamlit application
├── compare.py                 # PDF comparison logic
├── pdf_extractor.py           # PDF text extraction logic
├── text_preprocessing.py      # Preprocessing logic
│
├── LLM/                       # LLM integrations
│   ├── gemini.py              # Google Gemini API
│   ├── llama3.py              # LLAMA 3 via Ollama
│   └── prompt.py              # Prompt crafting
│
├── embeddings/                # Embedding techniques
│   ├── CountVectorizer.py
│   ├── TfidfVectorizer.py
│   └── all_MiniLM_L6_v2.py
│
├── result.py                  # Chatbot result formatting
├── requirements.txt           # Python dependencies
└── .env                       # Environment variables (not included)
```

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- [Streamlit](https://streamlit.io/) – Web UI framework  
- [Meta LLAMA 3](https://llama.meta.com/llama3/) – Open-weight large language model  
- [OLLAMA](https://ollama.com/) – Local LLM runner  
- [ChromaDB](https://www.trychroma.com/) – Vector database  
- [LangChain](https://www.langchain.com/) – LLM orchestration framework

---

## 👨‍💻 Author

**Vilas PK**  
GitHub: [@VILAS07](https://github.com/VILAS07)  
LinkedIn: [linkedin.com/in/vilaspk](https://www.linkedin.com/in/vilaspk)

---

> 💬 “Empowering radiology through AI-driven understanding and transparent comparison.”
```
