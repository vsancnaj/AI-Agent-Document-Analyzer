# **AI-Agent Document Analyzer**

This project is an **AI-powered document analysis bot** that processes and extracts information from PDF documents. It uses **LlamaIndex**, **LangChain**, and **Ollama** models to parse, analyze, and interact with document content. The bot intelligently handles user queries, retrieving only **relevant information** from the PDFs.

## **🚀 Why I Built This**
1. **To deepen my understanding of LLMs** by building a practical, hands-on project.
2. **To implement Retrieval-Augmented Generation (RAG)**, reducing hallucinations by feeding the model curated, factual data.
3. **To create a tool I wish I had during my thesis**—an AI that could compare and summarize research papers interactively.

This project is still **a work in progress**. I am continuously enhancing the bot by adding new tools and improving the **clarity and readability** of responses. Running a **local Ollama model** ensures **privacy** and eliminates API costs, allowing unrestricted experimentation.

---

## **✨ Features**
- **📄 PDF Parsing** – Extracts and interprets text from PDFs using `LlamaParse`.
- **🔍 Intelligent Querying** – Uses embeddings and vector search to **find only the most relevant** sections of documents.
- **📊 Vector Database** – Stores and retrieves information efficiently.
- **🤖 ReAct Agent** – Selects the appropriate tools to answer user queries dynamically.
- **💬 Interactive Chatbot** – Engages in real-time conversations about the documents.
- **🔗 Smart Link Extraction** – Extracts **only** the links relevant to the user’s query, not all links.

---

## **⚙️ Prerequisites**
Before running the project, ensure you’ve set up the environment:

### **1️⃣ Install Ollama (No API Key Needed)**
- Download and install **Ollama** (free & local).
- Verify Ollama is running:
    ```sh
    ollama list
    ```

### **2️⃣ Get a LlamaParse API Key (Free)**
- **Sign up for a key**: [LlamaParse](https://llamaindex.ai/)
- **Add it to your `.env` file**:
    ```plaintext
    LLAMA_PARSE_API_KEY=your_api_key
    ```

### **3️⃣ Use Local Embeddings (No API Key Required)**
- Ensure the embedding model is accessible:
    ```sh
    local:BAAI/bge-m3
    ```

---

## **📥 Installation**
1. **Clone the Repository**:
    ```sh
    git clone https://github.com/your-username/AI-Agent-Document-Analyzer.git
    cd AI-Agent-Document-Analyzer
    ```

2. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**:
    - Create a `.env` file.
    - Add your **LlamaParse API key**.

4. **Prepare Data**:
    - Place your **PDF documents** inside the `data` directory.

---

## **▶️ Usage**
Start the document analysis bot:
```sh 
python main.py
``` 
## **📝 Example Queries**
"Summarize this document."
"What are the key concepts discussed?"
"What is the objective of this research paper?"


## **🛠️ Code Overview**
| Component                 | Functionality                                              |
|---------------------------|----------------------------------------------------------|
| LlamaParse               | Parses PDFs into a structured format.                     |
| VectorStoreIndex         | Converts document text into embeddings for search.       |
| Query Engine             | Finds and retrieves only the most relevant sections.     |
| ReAct Agent              | Dynamically decides which tools to use based on queries. |
| Intent Classifier        | Determines if a query needs general info or links.       |
| Contextual Link Finder   | Extracts only the relevant links based on user queries.  |

## **🛠️ Future Improvements**
- Improve response formatting for better clarity.
- Enhance multi-document support.
- Integrate better summarization techniques for long documents.