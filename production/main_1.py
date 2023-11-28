import sys
from pathlib import Path
from code.export import fields_to_csv
from code.extraction import extract_fields
from code.ocr import texts_from_pdf

if __name__ == '__main__':
    data_directory: Path = Path(sys.argv[1])
    extracted_texts = texts_from_pdf(data_directory)
    extracted_fields = extract_fields(extracted_texts)
    if len(sys.argv) > 2:
        fields_to_csv(extracted_fields, save_path=Path(sys.argv[2]))

# working main.py
import sys
from pathlib import Path
from code.export import fields_to_csv
from code.extraction import extract_fields
from code.ocr import texts_from_pdf

if __name__ == '__main__':
    data_directory = Path(
        '/Users/lucazosso/Desktop/IE_Course/Hackathon/production/pdf_folder')
    extracted_texts = texts_from_pdf(data_directory)
    extracted_fields = extract_fields(extracted_texts)
    if len(sys.argv) > 2:
        fields_to_csv(extracted_fields, save_path=Path(sys.argv[2]))
    else:
        fields_to_csv(extracted_fields)
