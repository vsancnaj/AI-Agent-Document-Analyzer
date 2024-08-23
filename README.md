# AI-Agent Document Analyzer

This project is an AI-powered document analysis bot designed to process and extract information from PDF documents. It leverages the LlamaIndex library, LangChain, and Ollama models to parse, analyze, and interact with the content of these documents. The bot is capable of handling user queries and providing relevant information based on the PDFs it processes.

**My goal with this project is two fold: to deepen my understanding of large language models (LLMs) and to employ Retrieval-Augmented Generation (RAG) to mitigate hallucinations that can occur with these models. By feeding the model my own curated information, I aim to create a tool that works effectively for my needs.**

**I wish I had access to something like this during my thesis work—having a tool that could compare and answer questions about the numerous research papers I had to read on computer vision would have been invaluable. My vision is to develop this into a tool that facilitates interactive conversations between the model and the user about any document they provide.**

**Keep in mind!**
This project is still a work in progress. My goal is to continuously enhance the bot by adding more tools to the agent, making it increasingly useful. Currently, one of the main areas I am working on is improving the clarity and readability of the output. By using a local Ollama model, I not only benefit from enhanced privacy, but also from cost savings, allowing me to experiment freely without worrying about additional expenses.

## Features

- **PDF Parsing**: Parses and interprets text from PDF documents using `LlamaParse`.
- **Vector Embedding**: Converts document text into vector embeddings using a local model.
- **Vector Database**: Stores vectorized document data in a vector-based database, allowing for efficient and accurate querying.
- **Query Engine**: Utilizes the vector database to query and retrieve information from the documents.
- **ReAct Agent**: Uses a ReActAgent to determine the appropriate tools and actions to answer user queries.
- **Interactive Bot**: Engages in conversations, answering questions based on the content of the loaded documents.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/AI-Agent-Document-Analyzer.git
    cd AI-Agent-Document-Analyzer
    ```

2. **Install Dependencies**:
    Ensure that Python is installed on your system. Then, install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**:
    Create a `.env` file in the root directory and add any necessary API keys or configurations.

4. **Prepare Data**:
    Place your PDF documents in the `data` directory. The bot will parse and analyze these files.

## Usage

To start the document analysis bot, run:

```bash
python main.py
```
## Example Queries

- "What are the main key concepts of the documents?"
- "Summarize the content of the research paper."
- "What is the objective of the document?"

## Code Overview

- **LlamaParse**: Used to parse PDF documents into a format that the program can process.
- **VectorStoreIndex**: Converts document text into vectors and stores them in a vector-based database, allowing for efficient querying.
- **Query Engine**: Wraps the vector database to provide a powerful querying interface.
- **ReActAgent**: An agent that uses the llama3 model to handle reasoning and action decisions during interactions.
- **PromptTemplate**: Defines the format for the bot’s responses.
