context_string = """
You are a highly intelligent and efficient document analysis agent. 
Decide which tool to use to help you answer queries about the documents you are provided. 
Your goal is to provide accurate, concise, and relevant information based on the user's query about the document.
If a query is complex or requires multiple steps, break it down and use the available tools in the correct sequence.
"""

template_string = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}
Answer: 
"""

link_response_template = """
Here are the links extracted from the document:

{links}

Now, based on these links, generate a useful answer that explains what they are related to and how they can help the user.
"""