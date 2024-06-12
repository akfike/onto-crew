# tools/fileread_tools.py
import fitz  # PyMuPDF
from crewai_tools import tool

@tool("File Read Tool")
def file_read_tool(file_path: str, chunk_size: int = 1000) -> list:
    """Reads a PDF file and extracts its text content in chunks."""
    try:
        # Open the PDF file
        with fitz.open(file_path) as doc:
            text = ""
            for page in doc:
                text += page.get_text()

        # Split text into chunks
        chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
        return chunks
    except Exception as e:
        return [f"Fail to read the file {file_path}. Error: {str(e)}"]
