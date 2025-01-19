import os
import re
from dotenv import load_dotenv
from llama_index.llms.ollama import Ollama
from llama_parse import LlamaParse  # PDF parsing
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.embeddings import resolve_embed_model
from llama_index.core.tools import FunctionTool, QueryEngineTool, ToolMetadata

# ✅ Load environment variables
load_dotenv()
llama_api_key = os.getenv("LLAMA_PARSE_API_KEY")

# ✅ Initialize the LLMs
llm = Ollama(model="mistral", request_timeout=30.0)
intent_llm = Ollama(model="mistral", request_timeout=30.0)  # Used for intent classification

# ✅ Parse & Embed Documents Efficiently
parser = LlamaParse(api_key=llama_api_key, result_type="markdown")
file_extractor = {".pdf": parser}
data_path = os.path.join(os.path.dirname(__file__), '..', 'data')

documents = SimpleDirectoryReader(data_path, file_extractor=file_extractor).load_data()
embed_model = resolve_embed_model("local:BAAI/bge-m3")
vector_index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)

# ✅ Create a Query Engine for Efficient Retrieval
query_engine = vector_index.as_query_engine(llm=llm)

# ✅ Classify if the Query is Asking for Links
def classify_intent(query):
    """Determines if the user query is asking for links or general document information."""
    intent_prompt = f"""
    Analyze the following query: "{query}"
    Determine whether the user is asking for links, references, or external resources.
    Respond with a single word: "links" if they are, otherwise respond with "general".
    """

    # ✅ Call the LLM to classify the intent
    response = intent_llm.complete(intent_prompt)  # This returns a CompletionResponse object
    result_text = response.text.strip().lower()  # ✅ Extract the text before calling .strip()
    
    return result_text

# ✅ Define FunctionTool for Intent Classification
intent_classifier_tool = FunctionTool.from_defaults(
    classify_intent,
    name="intent_classifier",
    description="Classifies whether the user's query requires extracting links or general document retrieval."
)

# ✅ Extract Links from ONLY Relevant Sections
def extract_relevant_links(query):
    """Finds document sections related to the query and extracts links from those sections."""
    try:
        # ✅ Retrieve ONLY relevant sections based on the user query
        relevant_text = query_engine.query(f"Find sections related to '{query}' in the document.")

        # ✅ Extract links ONLY from those relevant sections
        url_pattern = r'https?://[^\s)]+'
        relevant_links = re.findall(url_pattern, relevant_text)

        return {
            "links": relevant_links if relevant_links else [],
            "message": f"Links relevant to '{query}' extracted successfully."
        }

    except Exception as e:
        return {"error": f"Failed to retrieve relevant links: {str(e)}"}

# ✅ Define FunctionTool for Finding RELEVANT Links
contextual_link_finder = FunctionTool.from_defaults(
    extract_relevant_links,
    name="contextual_link_finder",
    description="Finds document sections related to a user query and extracts relevant links from those sections."
)

# ✅ Register Tools for the AI Agent
tools = [
    intent_classifier_tool,  # Identifies intent
    QueryEngineTool(
        query_engine=query_engine,
        metadata=ToolMetadata(
            name="document_reader",
            description="Retrieves and interprets relevant sections from documents to answer questions accurately."
        ),
    ),
    contextual_link_finder  # Extracts ONLY relevant links based on query
]