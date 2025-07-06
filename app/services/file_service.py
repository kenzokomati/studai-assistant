import tempfile
from pathlib import Path
import pypdf
from fastapi import UploadFile

MAXIMUM_PAGE_RANGE = 25  # Maximum number of pages to extract from the PDF
MAXIMUM_PDF_LENGTH = 100000  # Maximum length of extracted content in characters
MAXIMUM_PDF_FILE_SIZE = 20 * 1024 * 1024  # Maximum PDF file size in bytes (10 MB)

def extract_pdf_content(file: UploadFile, start_page: int, end_page: int) -> str:
    if file.content_type != "application/pdf":
        raise ValueError("The uploaded file is not a valid PDF.")
    if file.size > MAXIMUM_PDF_FILE_SIZE:
        raise ValueError(f"The PDF file size exceeds the maximum limit of {MAXIMUM_PDF_FILE_SIZE} bytes.")
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(file.file.read())
        tmp_path = Path(tmp.name)
    reader = pypdf.PdfReader(tmp_path)

    pdf_length = len(reader.pages)

    if pdf_length == 0:
        raise ValueError("The PDF file is empty or has no readable pages.")
    if start_page < 0 or end_page > pdf_length or start_page >= end_page:
        raise ValueError(f"Invalid page range: start_page={start_page}, end_page={end_page}, total pages={pdf_length}.")
    if start_page == end_page:
        raise ValueError("Start page and end page cannot be the same.")
    if end_page - start_page > MAXIMUM_PAGE_RANGE + 1:
        raise ValueError(f"Cannot extract more than {MAXIMUM_PAGE_RANGE} pages at a time. Requested range: {end_page - start_page} pages.")
    
    content = []
    for page_num in range(start_page-1, end_page):
        page = reader.pages[page_num]
        text = page.extract_text()
        if text:
            content.append(text.strip())

    if not content:
        raise ValueError("No text could be extracted from the PDF file.")

    result = "\n".join(content)
    tmp_path.unlink(missing_ok=True)  # Clean up the temporary file

    if len(result) > MAXIMUM_PDF_LENGTH:
        raise ValueError(f"Extracted content exceeds the maximum length of {MAXIMUM_PDF_LENGTH} characters.")
    
    return result
