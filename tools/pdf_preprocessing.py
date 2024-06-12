import pandas as pd
import tiktoken

def read_and_tokenize_pdf(file_path: str, chunk_size: int = 800):
    """Reads a PDF file and extracts its text content in tokenized chunks."""
    try:
        import fitz  # PyMuPDF
        # Open the PDF file
        with fitz.open(file_path) as doc:
            text = ""
            for page in doc:
                text += page.get_text()

        # Initialize the GPT-3 tokenizer
        tokenizer = tiktoken.get_encoding("cl100k_base")

        # Tokenize the text
        tokens = tokenizer.encode(text)

        # Split tokens into chunks
        chunks = [tokens[i:i + chunk_size] for i in range(0, len(tokens), chunk_size)]

        # Decode chunks back to text
        chunk_texts = [tokenizer.decode(chunk) for chunk in chunks]

        return chunk_texts
    except Exception as e:
        return [f"Fail to read the file {file_path}. Error: {str(e)}"]

def read_and_tokenize_md(file_path: str, chunk_size: int = 800):
    """Reads a Markdown file and extracts its text content in tokenized chunks."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Initialize the GPT-3 tokenizer
        tokenizer = tiktoken.get_encoding("cl100k_base")

        # Tokenize the text
        tokens = tokenizer.encode(text)

        # Split tokens into chunks
        chunks = [tokens[i:i + chunk_size] for i in range(0, len(tokens), chunk_size)]

        # Decode chunks back to text
        chunk_texts = [tokenizer.decode(chunk) for chunk in chunks]

        return chunk_texts
    except Exception as e:
        return [f"Failed to read the file {file_path}. Error: {str(e)}"]

def read_and_tokenize_csv(file_path: str, chunk_size: int = 800):
    """Reads a CSV file and extracts its rows as tokenized tuples."""
    encodings = ['utf-8', 'latin1', 'iso-8859-1', 'cp1252']
    for encoding in encodings:
        try:
            # Read the CSV file into a pandas DataFrame
            df = pd.read_csv(file_path, encoding=encoding)
            
            # Convert each row to a tuple and then to a string for tokenization
            rows_as_strings = df.apply(tuple, axis=1).astype(str).tolist()

            # Combine all rows into a single text
            text = " ".join(rows_as_strings)

            # Initialize the GPT-3 tokenizer
            tokenizer = tiktoken.get_encoding("cl100k_base")

            # Tokenize the text
            tokens = tokenizer.encode(text)

            # Split tokens into chunks
            chunks = [tokens[i:i + chunk_size] for i in range(0, len(tokens), chunk_size)]

            # Decode chunks back to text
            chunk_texts = [tokenizer.decode(chunk) for chunk in chunks]

            return chunk_texts
        except Exception as e:
            continue  # Try the next encoding if the current one fails

    return [f"Failed to read the file {file_path}. Error: {str(e)}"]

def read_and_tokenize_txt(file_path: str, chunk_size: int = 800):
    """Reads a text file and extracts its text content in tokenized chunks."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Initialize the GPT-3 tokenizer
        tokenizer = tiktoken.get_encoding("cl100k_base")

        # Tokenize the text
        tokens = tokenizer.encode(text)

        # Split tokens into chunks
        chunks = [tokens[i:i + chunk_size] for i in range(0, len(tokens), chunk_size)]

        # Decode chunks back to text
        chunk_texts = [tokenizer.decode(chunk) for chunk in chunks]

        return chunk_texts
    except Exception as e:
        return [f"Failed to read the file {file_path}. Error: {str(e)}"]
