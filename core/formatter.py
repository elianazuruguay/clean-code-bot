import black
import os


def format_code(code: str, language: str) -> str:
    """
    Formats code depending on language.
    """

    if language == "python":
        return black.format_str(code, mode=black.FileMode())

    # No formatter available yet → return raw code
    elif language in ["javascript", "typescript", "java", "php"]:
        return code.strip()

    else:
        return code