import re
import ast


INJECTION_PATTERNS = [
    r"ignore (all|previous) instructions",
    r"system prompt",
    r"you are now",
    r"act as",
    r"reveal (api|key|secret)",
    r"delete (files|data)",
    r"sudo",
    r"rm -rf",
]

MAX_CODE_SIZE = 15000


class SecurityError(Exception):
    """Raised when a security violation is detected."""
    pass


def detect_prompt_injection(text: str) -> bool:
    """
    Detects potential prompt injection patterns in input text.

    Args:
        text (str): Input text to analyze.

    Returns:
        bool: True if injection patterns are detected, otherwise False.
    """
    lowered = text.lower()

    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, lowered):
            return True

    return False


def validate_syntax(code: str) -> None:
    """
    Validates that the provided Python code has correct syntax.

    Args:
        code (str): Python code to validate.

    Raises:
        SecurityError: If the code contains invalid Python syntax.
    """
    try:
        ast.parse(code)
    except SyntaxError:
        raise SecurityError("Invalid Python syntax detected")


def sanitize(code: str, language: str = "python") -> str:
    """
    Sanitizes input code depending on the programming language.

    Args:
        code (str): Source code to sanitize.
        language (str): Programming language of the code.

    Returns:
        str: Sanitized code.
    """
    code = code.replace("\x00", "")
    cleaned = code.strip()

    if len(cleaned) > MAX_CODE_SIZE:
        raise SecurityError("Code too large")

    if detect_prompt_injection(cleaned):
        raise SecurityError("Potential prompt injection detected")

    # Strict syntax checks currently supported for Python only.
    if language == "python":
        validate_syntax(cleaned)

    return cleaned