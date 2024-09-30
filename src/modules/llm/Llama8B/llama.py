"""A module to interact with the Llama API for academic journal questions."""

import json
import os
import sys

import pdfplumber
from openai import OpenAI

# Global thing for OpenAI client
client = None
conversation_history = []

def setup_client() -> None:
    """Set up the OpenAI client with an API key."""
    global client
    api_key = os.getenv("OPENAI_API_KEY")
    try:
        client = OpenAI(api_key=api_key, base_url="https://api.deepinfra.com/v1/openai")
    except Exception as e:
        print(f"Uh-oh, couldn't set up OpenAI client: {e}")
        sys.exit(1)  # If this fails, we're done here

# Snag some text from a PDF
def extract_text_from_pdf(file_path: str) -> str:
    """Grab text from a PDF with pdfplumber."""
    try:
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text()
        return text
    except FileNotFoundError:
        print(f"""Whoops, can't find the file: 
              {file_path}. Double-check it and try again.""")
        sys.exit(1)  # No file? No program.
    except Exception as e:
        print(f"Something went wrong pulling text from the PDF: {e}")
        sys.exit(1)  # If something else fails, bail out.

def upload_file(file_path: str) -> None:
    """Upload a file to Llama and save the content."""
    try:        
        # Get the file extension
        file_extension = os.path.splitext(file_path)[1].lower()
        
        file_content = ""
        
        if file_extension == ".json":
            try:
                with open(file_path) as f:
                    file_content = json.load(f).get(
                        "full-text-retrieval-response", {}).get("originalText")
            except FileNotFoundError:
                print(f"File's not here: {file_path}. Check your path.")
                sys.exit(1)
            except json.JSONDecodeError as e:
                print(f"Can't decode that JSON: {e}")
                sys.exit(1)
        elif file_extension == ".pdf":
            file_content = extract_text_from_pdf(file_path)
        else:
            print("Unsupported file type. Stick to .json or .pdf, please.")
            sys.exit(1)

        # Pop system and user messages into the conversation history
        conversation_history.append(
            {"role": "system",
             "content": "You're uploading an academic journal."})
        conversation_history.append(
            {"role": "user", "content": f"Remember this: {file_content}"})
        
        # Uploading the file content via Llama API
        response = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-8B-Instruct",
            messages=conversation_history
        )
        
        # Pulling the response
        response_content = response.choices[0].message.content.strip()
        
        # Stash assistant's reply in the history too
        conversation_history.append({"role": "assistant",
                                     "content": response_content})
        
        # If all went well
        if response_content:
            print("The file has been succesfully submitted.")
        else:
            print("API's acting weird. Check your inputs.")
            sys.exit(1)  # If the API didn't like it, we're out
    except Exception as e:
        print(f"Couldn't upload the file: {e}")
        sys.exit(1)  # Something went wrong

def query_llama(user_query: str) -> str:
    """Ask Llama a question and get the response."""
    try:
        # Add user's query to the history
        conversation_history.append({"role": "user", "content": user_query})
        
        # Send the question to Llama
        response = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-8B-Instruct",
            messages=conversation_history,
            #this might be a bit too low but the reponse may be quicker(?)
            temperature=0.1
        )

        # Pull out the response text
        output = response.choices[0].message.content.strip()
        
        # Put Llama's answer in the history too
        conversation_history.append({"role": "assistant", "content": output})
        
        return output
        
    except Exception as e:
        print(f"Llama couldn't answer that: {e}")
        sys.exit(1)  # If the query fails, no point in continuing

def clear_conversation_history() -> None:
    """Wipe the conversation history."""
    global conversation_history
    conversation_history = []

# Main loop for chatting
if __name__ == "__main__":
    # Set up OpenAI client first
    setup_client()
    
    # Ask for the file path and upload it
    file_path = input("Path to the file (.pdf or .json) you want to upload: ")
    upload_file(file_path)
    
    # Ready to chat
    print("Ask Llama a question or type 'exit' to leave.")
    
    while True:
        user_input = input("Query: ")
        
        # Leave if user says 'exit' #being forgiving
        if user_input.lower() == "exit" or user_input.lower() == "Exit":
            print("Bye amigos...")
            break
        
        # Ask Llama and print the answer
        response = query_llama(user_input)
        print(f"Assistant: {response}")
