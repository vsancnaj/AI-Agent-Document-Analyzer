import os
from dotenv import load_dotenv
from llama_index.llms.ollama import Ollama
from llama_index.core.agent import ReActAgent
from langchain_core.prompts import PromptTemplate
from prompts import context_string, template_string
from tools import tools, classify_intent, extract_relevant_links  # Import all tools

# ✅ Load environment variables
load_dotenv()

# ✅ Define the agent's LLM
agent_llm = Ollama(model="llama3")

# ✅ Allow the agent to dynamically pick tools
agent = ReActAgent.from_tools(
    tools, 
    llm=agent_llm, 
    verbose=True, 
    context=context_string
)

# ✅ Define the prompt template
output_prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=template_string
)

def process_extracted_links(result):
    """Formats extracted links for better readability."""
    if isinstance(result, dict) and "links" in result:
        links = result["links"]
        if not links:
            return "No relevant links found."

        formatted_links = "\n".join([f"- {link}" for link in links])
        return f"Here are the relevant links:\n{formatted_links}"

    return str(result)

def handle_conversation():
    context = ""
    print("Welcome to the AI Document Analysis Bot! Type 'q' to quit.")

    while (user_input := input("You: ")) != 'q':
        try:
            # ✅ Let the agent classify the intent of the query
            intent = classify_intent(user_input)

            if intent == "links":
                result = extract_relevant_links(user_input)  # Extract only relevant links
            else:
                result = agent.chat(user_input)  # Default to general document query

            formatted_result = process_extracted_links(result)
            formatted_output = output_prompt.format(context=context, question=user_input)
            answer = formatted_output + formatted_result

            print("Bot:", answer)
            context += f"\nUser: {user_input}\nAI: {formatted_result}\n"

        except ValueError as e:
            print(f"An error occurred: {e}")
            print("Bot: I'm sorry, I couldn't process that. Could you please try again?")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Bot: I'm sorry, something went wrong.")

if __name__ == "__main__":
    handle_conversation()