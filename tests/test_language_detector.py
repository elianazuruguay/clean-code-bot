from core.language_detector import detect_language


def test_detect_language_returns_mapped_language():
    assert detect_language("main.py") == "python"
    assert detect_language("app.ts") == "typescript"


def test_detect_language_returns_unknown_for_unmapped_extension():
    assert detect_language("README.md") == "unknown"
