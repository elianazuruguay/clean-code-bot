import os
from config.language_config import LANGUAGE_CONFIG

ALLOWED_EXTENSIONS = [
    ext
    for exts in LANGUAGE_CONFIG.values()
    for ext in exts
]

class FileValidationError(Exception):
    """Custom exception for file validation errors."""
    pass


def validate_file(file_path: str) -> bool:
    """
    Validates:
    1. File exists
    2. File extension is allowed
    """

    if not os.path.exists(file_path):
        raise FileValidationError(
            f"File not found: {file_path}"
        )

    _, ext = os.path.splitext(file_path)

    if ext not in ALLOWED_EXTENSIONS:
        raise FileValidationError(
            f"Extension '{ext}' not supported. Allowed: {ALLOWED_EXTENSIONS}"
        )

    return True