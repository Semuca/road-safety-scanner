#this version: accept .json and .pdf files, rename the file to DOI if not yet named with DOI, and query the GPT model with the file content.
import os
import json
import pdfplumber
from openai import OpenAI

GPT_API_KEY = os.environ.get('GPT_API_KEY')

client = OpenAI(api_key='GPT_API_KEY')

conversation_history = []

def extract_doi_from_json(file_path: str) -> str:
    try:
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

            #DOI tend to be stored in this path in the file. So far works well 
            if "full-text-retrieval-response" in data and "coredata" in data["full-text-retrieval-response"] and "prism:doi" in data["full-text-retrieval-response"]["coredata"]:
                doi = data.get("full-text-retrieval-response", {}).get("coredata", {}).get("prism:doi")
                return doi

            print("DOI not found in the JSON file.")
            return None

    except Exception as e:
        print(f"There was an issue extracting the DOI: {e}")
        return None

def extract_text_from_pdf(file_path: str) -> str:
    try:
        with pdfplumber.open(file_path) as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        print(f"There was an issue extracting text from the PDF: {e}")
        return None

def extract_doi_from_pdf(file_path: str) -> str:
    try:
        text = extract_text_from_pdf(file_path)
        if text:
            start_index = text.find('DOI:' or 'doi:') 
            if start_index != -1:
                doi = text[start_index+4:].split()[0]
                return doi.strip()
        print("DOI not found in the PDF file.")
        return None
    except Exception as e:
        print(f"There was an issue extracting the DOI from the PDF: {e}")
        return None

def rename_file_if_needed(file_path: str, doi: str) -> str:

    if not doi.startswith("10."):
        print("Invalid DOI format. DOI must start with '10.'")
        return file_path

    try:
        directory, original_filename = os.path.split(file_path)
        file_extension = os.path.splitext(file_path)[1].lower()
        expected_filename = doi.replace("/", "-") + file_extension
        expected_file_path = os.path.join(directory, expected_filename)

        if original_filename != expected_filename:
            os.rename(file_path, expected_file_path)
            print(f"Renaming file from '{original_filename}' to '{expected_filename}'")
            return expected_file_path
        return file_path
    
    except Exception as e:
        print(f"There was an issue renaming the file: {e}")
        return file_path

def uploadFile() -> str:
    try:
        file_path = input("Enter the file path: ")
        file_extension = os.path.splitext(file_path)[1].lower()

        if file_extension == ".json":
            doi = extract_doi_from_json(file_path)
            if doi:
                file_path = rename_file_if_needed(file_path, doi)
                print("File renaming successful.")
            return file_path
        elif file_extension == ".pdf":
            doi = extract_doi_from_pdf(file_path)
            if doi:
                file_path = rename_file_if_needed(file_path, doi)
                print("File renaming successful.")
            return file_path
        else:
            print("Unsupported file type. Please upload a .json or .pdf file.")
            return None
    except Exception as e:
        print(f"There was an issue uploading the file: {e}")
        return None

def queryGPT(file_path: str) -> None:
    try:
        file_extension = os.path.splitext(file_path)[1].lower()

        if file_extension == ".json":
            with open(file_path, 'r', encoding='utf-8') as f:
                file_content = f.read()
        elif file_extension == ".pdf":
            file_content = extract_text_from_pdf(file_path)
        else:
            print("Unsupported file type for querying GPT.")
            return

        conversation_history = [
            {"role": "system", "content": "You are uploading an academic journal."},
            {"role": "user", "content": f"Please remember the following content: {file_content}"}
        ]

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation_history,
            temperature=0.5
        )

        response_content = response.choices[0].message.content.strip()
        conversation_history.append({"role": "assistant", "content": response_content})

        if response_content:
            print("File content uploaded and stored successfully.")
        else:
            print("Unexpected response from API. Please check the file input.")

        while True:
            user_query = input("Enter your query ('exit' to quit): ")

            if user_query.lower() in ["exit", "Exit", "'exit'", "quit"]: #trying to be kind
                print("Exiting... bye amigos")
                break

            conversation_history.append({"role": "user", "content": user_query})

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=conversation_history,
                temperature=0.5 
            )

            output = response.choices[0].message.content.strip()
            conversation_history.append({"role": "assistant", "content": output})

            print(output)

    except Exception as e:
        print(f"There was an issue querying the GPT model: {e}")

file_path = uploadFile()

if file_path:
    print("Uploading the file...")
    queryGPT(file_path)
