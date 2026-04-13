import os
from config.language_config import LANGUAGE_CONFIG


EXT_TO_LANGUAGE = {
    ext: lang
    for lang, exts in LANGUAGE_CONFIG.items()
    for ext in exts
}


def detect_language(file_path: str) -> str:
    """
    Detect programming language based on file extension.

    Args:
        file_path (str): Path to source file.

    Returns:
        str: Detected language or 'unknown'.
    """
    _, ext = os.path.splitext(file_path)
    return EXT_TO_LANGUAGE.get(ext, "unknown")