from pathlib import Path
from pypdf import PdfReader

def load_document(folder_path):
    document=[]
    folder = Path(folder_path)
    for file_path in folder.glob("*.pdf"):
        reader = PdfReader(file_path)
        
        for page_number, page in enumerate(reader.pages, start=1):
            text = page.extract_text()
            
            if text:
                document.append({
                    "text":text,
                    "source":file_path.name,
                    "page":page_number
                })
    return document

            
    