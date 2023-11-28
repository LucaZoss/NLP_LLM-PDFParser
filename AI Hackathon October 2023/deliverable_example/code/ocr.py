from pathlib import Path
from typing import Dict


def texts_from_pdf(data_directory: Path) -> Dict[str, str]:
    return {"doc_1": "text_1", "doc_2": "text_2"}
