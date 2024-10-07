import json
import os
import pdfplumber
import sys
from openai import OpenAI

"""Shared functions"""

def extract_text_from_pdf(file_path: str) -> str:
    """Extract text from a PDF file using pdfplumber."""
    try:
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text()
        return text
    except Exception:
        return ""


"""GPT functions and globals """

class OpenAIGPTClient:
    """A class to interact with the OpenAI GPT model using OpenAI's API."""

    def __init__(self, model: str, api_key: str) -> None:
        """Set up the OpenAI client with the provided API key."""
        self.model = model
        self.client = OpenAI(api_key=api_key)
        self.conversation_history = []

    def upload_file(self, file_path: str) -> None:
        """Upload file to the OpenAI GPT model and store the content."""
        try:        
            file_extension = os.path.splitext(file_path)[1].lower()
            file_content = ""

            if file_extension == ".json":
                with open(file_path) as f:
                    file_content = json.load(f).get("full-text-retrieval-response", {}).get("originalText")
            elif file_extension == ".pdf":
                file_content = extract_text_from_pdf(file_path)
            else:
                return

            self.conversation_history.append(
                {"role": "system", "content": "You are uploading an academic journal."}
            )
            self.conversation_history.append(
                {"role": "user", "content": f"Please remember the following content: {file_content}"}
            )

            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.conversation_history,
                temperature=0.1
            )

            response_content = response.choices[0].message.content.strip()
            self.conversation_history.append({"role": "assistant", "content": response_content})
        except Exception as e:
            print(f"There was an issue uploading the file content to OpenAI GPT: {e}")

    def query(self, user_query: str) -> str:
        """Query the GPT model with the user input and return the response."""
        try:
            self.conversation_history.append({"role": "user", "content": user_query})

            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.conversation_history,
                temperature=0.1
            )

            output = response.choices[0].message.content.strip()
            self.conversation_history.append({"role": "assistant", "content": output})

            return output
        except Exception as e:
            print(f"There was an issue querying the OpenAI GPT model: {e}")

    def clear_conversation_history(self) -> None:
        """Clear the conversation history."""
        self.conversation_history = []


"""Llama8B functions and globals """

client = None
conversation_history = []

def setup_llama_client() -> None:
    """Set up the Llama client with an API key."""
    global client
    api_key = os.getenv("LLAMA_API_KEY")
    try:
        client = OpenAI(api_key=api_key, base_url="https://api.deepinfra.com/v1/openai")
    except Exception as e:
        print(f"Uh-oh, couldn't set up Llama client: {e}")
        sys.exit(1)

def upload_file_llama(file_path: str) -> None:
    """Upload a file to Llama and save the content."""
    try:        
        file_extension = os.path.splitext(file_path)[1].lower()
        file_content = ""

        if file_extension == ".json":
            try:
                with open(file_path) as f:
                    file_content = json.load(f).get("full-text-retrieval-response", {}).get("originalText")
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

        conversation_history.append(
            {"role": "system", "content": "You're uploading an academic journal."}
        )
        conversation_history.append(
            {"role": "user", "content": f"Remember this: {file_content}"}
        )

        response = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-8B-Instruct",
            messages=conversation_history
        )

        response_content = response.choices[0].message.content.strip()
        conversation_history.append({"role": "assistant", "content": response_content})

        if response_content:
            print("The file has been successfully submitted.")
        else:
            print("API's acting weird. Check your inputs.")
            sys.exit(1)
    except Exception as e:
        print(f"Couldn't upload the file to Llama API: {e}")
        sys.exit(1)

def query_llama(user_query: str) -> str:
    """Ask Llama a question and get the response."""
    try:
        conversation_history.append({"role": "user", "content": user_query})

        response = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-8B-Instruct",
            messages=conversation_history,
            temperature=0.1
        )

        output = response.choices[0].message.content.strip()
        conversation_history.append({"role": "assistant", "content": output})

        return output
    except Exception as e:
        print(f"Llama couldn't answer that: {e}")
        sys.exit(1)

def clear_llama_conversation_history() -> None:
    """Wipe the conversation history."""
    global conversation_history
    conversation_history = []

""" Main """

if __name__ == "__main__":
    model_choice = input("Choose model (1 for GPT-4o mini, 2 for Llama 8B): ")

    if model_choice == "1":
        openai_client = OpenAIGPTClient(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
        file_path = input("Path to the file (.pdf or .json) you want to upload: ")
        openai_client.upload_file(file_path)

        print("Ask a question or type 'exit' to quit.")
        while True:
            user_input = input("Query: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Exiting...")
                break
            response = openai_client.query(user_input)
            print(f"Assistant: {response}")

    elif model_choice == "2":
        setup_llama_client()
        file_path = input("Path to the file (.pdf or .json) you want to upload: ")
        upload_file_llama(file_path)

        print("Ask Llama a question or type 'exit' to quit.")
        while True:
            user_input = input("Query: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Exiting...")
                break
            response = query_llama(user_input)
            print(f"Assistant: {response}")
