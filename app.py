import os
import streamlit as st
from pathlib import Path
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# 加载环境变量
load_dotenv()

# 设置页面
st.set_page_config(page_title="AI知识库", layout="wide")
st.title("📚 我的 AI 知识库")

# 初始化会话状态
if "knowledge_base" not in st.session_state:
    st.session_state.knowledge_base = None
if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = []

# 侧边栏：上传文件
st.sidebar.header("📤 上传文件")
uploaded_files = st.sidebar.file_uploader(
    "上传 PDF 文件",
    type="pdf",
    accept_multiple_files=True
)

# 处理上传的文件
if uploaded_files:
    if st.sidebar.button("🔄 构建知识库"):
        with st.spinner("正在处理文件..."):
            try:
                # 保存上传的文件
                temp_dir = Path("temp_uploads")
                temp_dir.mkdir(exist_ok=True)
                
                documents = []
                for uploaded_file in uploaded_files:
                    file_path = temp_dir / uploaded_file.name
                    with open(file_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    
                    loader = PyPDFLoader(str(file_path))
                    docs = loader.load()
                    documents.extend(docs)
                
                # 拆分文本
                text_splitter = RecursiveCharacterTextSplitter(
                    chunk_size=500,
                    chunk_overlap=50
                )
                split_docs = text_splitter.split_documents(documents)
                
                # 创建嵌入和知识库
                embeddings = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
                
                st.session_state.knowledge_base = Chroma.from_documents(
                    documents=split_docs,
                    embedding=embeddings,
                    persist_directory="./chroma_db"
                )
                st.session_state.uploaded_files = [f.name for f in uploaded_files]
                
                st.sidebar.success("✅ 知识库构建成功！")
                
            except Exception as e:
                st.sidebar.error(f"❌ 错误: {str(e)}")

# 显示已上传的文件
if st.session_state.uploaded_files:
    st.sidebar.subheader("📋 已上传文件:")
    for file_name in st.session_state.uploaded_files:
        st.sidebar.text(f"✓ {file_name}")

# 主界面：提问
st.header("💬 向 AI 提问")

if st.session_state.knowledge_base is None:
    st.info("👈 请先在左边上传 PDF 文件，然后点击'构建知识库'")
else:
    question = st.text_input("请输入你的问题:")
    
    if question:
        with st.spinner("思考中..."):
            try:
                # 在知识库中搜索相关文档
                docs = st.session_state.knowledge_base.similarity_search(question, k=3)
                
                # 初始化 Claude
                llm = ChatOpenAI(
    api_key="sk-96487196d97c43878d55b15a2b782ee5",
    base_url="https://api.deepseek.com",
    model="deepseek-chat"
)
                
                # 构建提示词
                context = "\n".join([doc.page_content for doc in docs])
                prompt = f"""基于以下文档内容，回答用户的问题。

文档内容：
{context}

用户问题：{question}

请根据文档内容回答，如果文档中没有相关信息，请说明。"""
                
                # 获取答案
                response = llm.invoke(prompt)
                
                # 显示答案
                st.subheader("🤖 AI 的回答:")
                st.write(response.content)
                
                # 显示来源
                st.subheader("📖 来源文档:")
                if docs:
                    for i, doc in enumerate(docs, 1):
                        with st.expander(f"来源 {i} - {doc.metadata.get('source', 'Unknown')}"):
                            st.write(doc.page_content)
                            st.caption(f"页码: {doc.metadata.get('page', 'N/A')}")
                
            except Exception as e:
                st.error(f"❌ 错误: {str(e)}")