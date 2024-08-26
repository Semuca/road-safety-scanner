import os
import PyPDF2
import pdfplumber
from openai import OpenAI

GPT_API_KEY = os.environ.get('GPT_API_KEY')

client = OpenAI(api_key=GPT_API_KEY)

conversation_history = []

# Function to extract text from a PDF file
def extract_text_from_pdf(file_path: str) -> str:
    """Extract text from a PDF file using pdfplumber."""
    try:
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        print(f"There was an issue extracting text from the PDF file: {e}")
        return ""

'''
#V1, filepath predefined.
def uploadFile(file: str) -> None:
    try:
        # Open and read the file content
        with open(file, 'r', encoding='utf-8') as f:
            file_content = f.read()

        # Add the system and user messages to the conversation history
        conversation_history.append({"role": "system", "content": "You are uploading an academic journal."})
        conversation_history.append({"role": "user", "content": f"Please remember the following content: {file_content}"})
        
        # Store the file content using OpenAI's API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation_history
        )
        
        # Extracting and printing the response for debugging
        response_content = response.choices[0].message.content.strip()
        
        # Add the assistant's response to the conversation history
        conversation_history.append({"role": "assistant", "content": response_content})
        
        # Check for successful completion
        if response_content:
            print("File content uploaded and stored successfully.")
        else:
            print("Unexpected response from API. Please check the input data.")
    except Exception as e:
        print(f"There was an issue uploading the file content: {e}")
        
'''
#V2, allowing user to input their own filepath, check file extension, if pdf then convert.
def uploadFile() -> None:
    try:
        # Prompt the user to enter the file path
        file_path = input("Please enter the file path: ")
        
        # Check the file extension
        file_extension = os.path.splitext(file_path)[1].lower()
        
        # Initialize the file content variable
        file_content = ""
        
        if file_extension == ".txt":
            # Open and read the text file content
            with open(file_path, 'r', encoding='utf-8') as f:
                file_content = f.read()
        elif file_extension == ".pdf":
            # Extract text from the PDF file
            file_content = extract_text_from_pdf(file_path)
        else:
            print("Unsupported file type. Please upload a .txt or .pdf file.")
            return

        # Add the system and user messages to the conversation history
        conversation_history.append({"role": "system", "content": "You are uploading an academic journal."})
        conversation_history.append({"role": "user", "content": f"Please remember the following content: {file_content}"})
        
        # Store the file content using OpenAI's API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation_history
        )
        
        # Extracting and printing the response for debugging
        response_content = response.choices[0].message.content.strip()
        
        # Add the assistant's response to the conversation history
        conversation_history.append({"role": "assistant", "content": response_content})
        
        # Check for successful completion
        if response_content:
            print("File content uploaded and stored successfully.")
        else:
            print("Unexpected response from API. Please check the input data.")
    except Exception as e:
        print(f"There was an issue uploading the file content: {e}")


'''
#V1, pre-defined query.
def queryGPT(query: str) -> str:
    try:
        # Add the user query to the conversation history
        conversation_history.append({"role": "user", "content": query})
        
        # Query the GPT model with the user input
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation_history
        )

        # Extract the response content
        output = response.choices[0].message.content.strip()
        
        # Add the assistant's response to the conversation history
        conversation_history.append({"role": "assistant", "content": output})
        
        return output
    except Exception as e:
        return f"There was an issue querying the GPT model: {e}"

uploadFile('test1.txt')

# Querying GPT with a question
result = queryGPT("Can you provide a brief summary of the key points?")
print(result)
'''

'''
#V2, allowing user to input their own queries.
def queryGPT() -> str:
    try:
        # Get user input
        user_query = input("Please enter your query: ")
        
        # Add the user query to the conversation history
        conversation_history.append({"role": "user", "content": user_query})
        
        # Query the GPT model with the user input
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation_history
        )

        # Extract the response content
        output = response.choices[0].message.content.strip()
        
        # Add the assistant's response to the conversation history
        conversation_history.append({"role": "assistant", "content": output})
        
        return output
    except Exception as e:
        return f"There was an issue querying the GPT model: {e}"

uploadFile('test1.txt')

# Querying GPT with a question
result = queryGPT()
print(result)
'''
#V3, allowing user to input their own queries plus implementing while loop so can take more than one queries unil 'exit' typed.
def queryGPT() -> str:
    try:
        while True:
            # Get user input
            user_query = input("Enter your query ('exit' to quit): ")

            if user_query.lower() in ["exit", "quit"]:
                print("Exiting... bye amigos")
                break
            
            # Add the user query to the conversation history
            conversation_history.append({"role": "user", "content": user_query})
            
            # Query the GPT model with the user input
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=conversation_history
            )

            # Extract the response content
            output = response.choices[0].message.content.strip()
            
            # Add the assistant's response to the conversation history
            conversation_history.append({"role": "assistant", "content": output})
            
            print(output)
            
    except Exception as e:
        print(f"There was an issue querying the GPT model: {e}")

uploadFile()

queryGPT()