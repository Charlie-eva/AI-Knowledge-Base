```markdown
# 🤖 AI Knowledge Base

An AI-powered knowledge base application that enables users to upload PDF documents and ask intelligent questions about them using RAG (Retrieval-Augmented Generation) technology.

## ✨ Features

- **PDF Upload**: Support for multiple PDF file uploads
- **Smart Q&A**: Ask questions about your documents in natural language
- **RAG Technology**: Retrieves relevant content before generating answers for accuracy
- **Source Attribution**: Shows which document sections the AI used to answer your questions
- **Real-time Processing**: Instant document analysis and indexing
- **User-Friendly Interface**: Clean, intuitive web interface built with Streamlit

## 🛠️ Tech Stack

- **Frontend**: Streamlit - Python web framework for fast UI development
- **Backend**: Python 3.14
- **Vector Database**: Chroma - for semantic search and document storage
- **LLM Integration**: LangChain - orchestrates AI pipeline
- **Large Model**: DeepSeek API - Chinese-optimized language model
- **Text Processing**: PyPDF, RecursiveCharacterTextSplitter

## 🚀 How It Works

### RAG Pipeline:
1. **Document Upload**: User uploads PDF files
2. **Text Extraction**: PyPDF extracts text from documents
3. **Chunking**: Text is split into semantic chunks (500 tokens, 50 token overlap)
4. **Vectorization**: HuggingFace embeddings convert chunks to vectors
5. **Storage**: Vectors stored in Chroma vector database
6. **Query Processing**: User questions are vectorized
7. **Retrieval**: Top 3 relevant chunks retrieved via similarity search
8. **Generation**: DeepSeek generates answers based on retrieved context
9. **Attribution**: Sources and page numbers displayed to user

## 📦 Installation

### Prerequisites
- Python 3.10+
- pip

### Setup

```bash
# Clone repository
git clone https://github.com/Charlie-eva/AI-Knowledge-Base.git
cd AI-Knowledge-Base

# Create virtual environment
python -m venv venv
source venv/Scripts/activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "DEEPSEEK_API_KEY=your_api_key_here" > .env
```

## 🎯 Usage

```bash
# Activate virtual environment
source venv/Scripts/activate  # Windows: venv\Scripts\activate

# Run application
streamlit run app.py

# Open browser to http://localhost:8501
```

### How to Use:
1. Click "Browse files" to upload PDF documents
2. Click "构建知识库" (Build Knowledge Base) to process documents
3. Type your question in the input box
4. AI generates answer with source citations

## 💡 Key Skills Demonstrated

✅ **AI/ML Concepts**: RAG, vector embeddings, semantic search, prompt engineering
✅ **Python Development**: Full-stack Python application development
✅ **API Integration**: Working with external LLM APIs and authentication
✅ **Data Processing**: PDF parsing, text chunking, vector transformations
✅ **Database**: Vector database operations and similarity search
✅ **UI/UX**: User interface design with Streamlit
✅ **DevOps**: Virtual environments, dependency management, version control

## 📋 Project Structure

```
AI-Knowledge-Base/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                   # API keys (not committed)
├── .gitignore            # Git ignore rules
├── chroma_db/            # Vector database storage
└── temp_uploads/         # Temporary PDF storage
```

## 🔧 Configuration

Edit `.env` file to add your DeepSeek API key:

```
DEEPSEEK_API_KEY=sk-your-key-here
```

## 📈 Future Enhancements

- [ ] Support for more document formats (DOCX, TXT, images with OCR)
- [ ] Multi-language support
- [ ] User authentication and saved conversations
- [ ] Batch processing for large document collections
- [ ] Custom model fine-tuning
- [ ] Export chat history functionality
- [ ] Advanced filtering and search options

## 🎓 Learning Outcomes

Through this project, I learned:
- How to build end-to-end AI applications
- RAG architecture and implementation
- Vector database operations
- LLM API integration
- Full-stack Python development
- UI/UX best practices for AI applications

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**Charlie-eva**
- GitHub: [@Charlie-eva](https://github.com/Charlie-eva)

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Last Updated**: March 2026
