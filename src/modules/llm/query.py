"""Utility functions to interact with the LLM models using OpenAI's API."""

import json
import os
from typing import Self

import pdfplumber
from openai import OpenAI


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

class OpenAIClient:
    """A class to interact with the OpenAI GPT model using OpenAI's API."""

    def __init__(self: Self, model: str, api_key: str, url: str = None) -> None:
        """Set up the OpenAI client with the provided API key."""
        self.model = model
        self.client = OpenAI(api_key=api_key, base_url=url)
        self.conversation_history = []

    def upload_file(self: Self, file_path: str) -> None:
        """Upload file to the OpenAI GPT model and store the content."""
        try:        
            file_extension = os.path.splitext(file_path)[1].lower()
            file_content = ""

            if file_extension == ".json":
                with open(file_path) as f:
                    file_content = json.load(f).get(
                        "full-text-retrieval-response", {}).get("originalText")
            elif file_extension == ".pdf":
                file_content = extract_text_from_pdf(file_path)
            else:
                return

            self.conversation_history.append(
                {"role": "system",
                 "content": "You are uploading an academic journal."}
            )
            self.conversation_history.append(
                {"role": "user",
                 "content":
                 f"Please remember the following content: {file_content}"}
            )

            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.conversation_history,
                temperature=0.1
            )

            response_content = response.choices[0].message.content.strip()
            self.conversation_history.append(
                {"role": "assistant", "content": response_content})
        except Exception as e:
            print(
                f"There was an issue uploading the file content to OpenAI: {e}")

    def query(self: Self, user_query: str) -> str:
        """Query the GPT model with the user input and return the response."""
        try:
            self.conversation_history.append(
                {"role": "user", "content": user_query})

            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.conversation_history,
                temperature=0.1
            )

            output = response.choices[0].message.content.strip()
            self.conversation_history.append(
                {"role": "assistant", "content": output})

            return output
        except Exception as e:
            print(f"There was an issue querying the OpenAI model: {e}")

    def clear_conversation_history(self: Self) -> None:
        """Clear the conversation history."""
        self.conversation_history = []
