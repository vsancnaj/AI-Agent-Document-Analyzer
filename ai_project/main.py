from llama_index.llms.ollama import Ollama
from llama_parse import LlamaParse # parsing of pdf
from langchain_core.prompts import PromptTemplate
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.embeddings import resolve_embed_model

from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from dotenv import load_dotenv
from prompts import context_string, template_string
import os

# load any API key from .env file found in the directory
load_dotenv()
# using the mistral ollama model
llm = Ollama(model="mistral", request_timeout=30.0)
# converting the document text into a format that can be used by the program
parser = LlamaParse(result_type="markdown")
# extracting files that are solely PDF
file_extractor = {".pdf": parser}
# specifing the data path to retrieve the documents from
data_path = os.path.join(os.path.dirname(__file__), '..', 'data')
# loading files and parsing them
documents = SimpleDirectoryReader(data_path, file_extractor=file_extractor).load_data()
# print("Loaded documents:", documents)

# embedding the document and converting them into vectores
embed_model = resolve_embed_model("local:BAAI/bge-m3") # access to the local model to create the vector embeddings
# creating a vector based database
vector_index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)
 # wraps the index into a query engine
query_engine = vector_index.as_query_engine(llm=llm)

# tools the agent will use
tools = [
    QueryEngineTool(
        query_engine=query_engine,
        metadata=ToolMetadata(
            name="document_reader",
            description="This tool extracts and interprets text from any PDF document, including books, research papers, contracts, and more. Use it to read, analyze, and understand content within PDF files across a wide range of topics.",
        )
    )
]
# the ollama model the agent will use
agent_llm = Ollama(model="llama3")
# reasoning then action agent initialisation
agent = ReActAgent.from_tools(tools, llm=agent_llm, verbose=True, context=context_string)

# Define the prompt template
output_prompt = PromptTemplate(
    input_variables = ["context", "question"],
    template = template_string
    )

def handle_conversation():
    context = ""
    print("Welcome to the Document Analysis Bot!. Type 'q' to quit.")
    
    while (user_input := input("You: ")) != 'q':
        try:
            # Run the agent with the current context and user input
            result = agent.chat(user_input)
            
            # Format the output using the template
            formatted_output = output_prompt.format(context=context, question=user_input)
            answer = formatted_output + str(result)  # Combine the formatted prompt with the result
            
            # Output the result from the agent
            print("Bot: ", answer)
            
            # Update the context with the user input and agent response
            context += f"\nUser: {user_input}\nAI: {result}\n"

        except ValueError as e:
            print(f"An error occurred: {e}")
            print("Bot: I'm sorry, I couldn't process that. Could you please try again?")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Bot: I'm sorry, something went wrong.")

if __name__ == "__main__":
    handle_conversation()
    
# what are the main key concepts of the documents?