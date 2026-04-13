from core.formatter import format_code


def test_format_code_formats_python_with_black():
    result = format_code("def add(a,b):\n return a+b\n", "python")
    assert "def add(a, b):" in result
    assert "return a + b" in result


def test_format_code_strips_supported_non_python_languages():
    result = format_code("  const x = 1;  ", "javascript")
    assert result == "const x = 1;"


def test_format_code_returns_raw_for_unknown_languages():
    raw = "  <xml/>  "
    assert format_code(raw, "xml") == raw
