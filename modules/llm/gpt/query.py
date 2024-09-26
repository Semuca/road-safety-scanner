"""Utility functions to interact with the GPT model using OpenAI's API."""

import json
import os

import pdfplumber
from openai import OpenAI

client = None

def setup_client(api_key: str) -> None:
    """Set up the OpenAI client with the provided API key."""
    global client
    client = OpenAI(api_key=api_key)

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

def upload_file(file_path: str) -> None:
    """Upload file to the GPT model and store the content."""
    try:        
        # Check the file extension
        file_extension = os.path.splitext(file_path)[1].lower()
        
        # Initialize the file content variable
        file_content = ""
        
        if file_extension == ".json":
            # Open and read the json file content
            with open(file_path) as f:
                file_content = json.load(f).get("full-text-retrieval-response",
                                                {}).get("originalText")
        elif file_extension == ".pdf":
            # Extract text from the PDF file
            file_content = extract_text_from_pdf(file_path)
        else:
            print("Unsupported file type. Please upload a .json or .pdf file.")
            return

        # Add the system and user messages to the conversation history
        conversation_history.append({"role": "system",
                        "content": "You are uploading an academic journal."})
        conversation_history.append({"role": "user",
        "content": f"Please remember the following content: {file_content}"})
        
        # Store the file content using OpenAI's API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation_history
        )
        
        # Extracting the response
        response_content = response.choices[0].message.content.strip()
        
        # Add the assistant's response to the conversation history
        conversation_history.append({"role": "assistant",
                                     "content": response_content})
        
        # Check for successful completion
        if response_content:
            print("File content uploaded and stored successfully.")
        else:
            print("Unexpected response from API. Please check the input data.")
    except Exception as e:
        print(f"There was an issue uploading the file content: {e}")


def query_gpt(user_query: str) -> str:
    """Query the GPT model with the user input and return the response."""
    try:
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
        print(f"There was an issue querying the GPT model: {e}")

def clear_conversation_history() -> None:
    """Clear the conversation history."""
    global conversation_history
    conversation_history = []
