import core.processor as processor_module
from core.processor import CodeProcessor


class FakeEngine:
    def __init__(self, llm):
        self.llm = llm

    def analyze(self, code: str, language: str) -> str:
        return f"analysis:{language}:{code}"

    def plan(self, analysis: str, language: str) -> str:
        return f"plan:{language}:{analysis}"

    def generate(self, plan: str, language: str) -> str:
        return "```python\nprint('ok')\n```"


def test_clean_output_removes_markdown_fences():
    text = "```python\nprint('hello')\n```"
    assert CodeProcessor._clean_output(text) == "print('hello')"


def test_process_file_happy_path_with_output_override(tmp_path, monkeypatch):
    input_file = tmp_path / "before.py"
    output_file = tmp_path / "after.py"
    input_file.write_text("print('x')\n", encoding="utf-8")

    monkeypatch.setattr(processor_module, "PromptEngine", FakeEngine)
    monkeypatch.setattr(processor_module, "detect_language", lambda _: "python")
    monkeypatch.setattr(processor_module, "validate_file", lambda _: True)
    monkeypatch.setattr(processor_module, "sanitize", lambda code, language: code.strip())
    monkeypatch.setattr(processor_module, "format_code", lambda code, language: f"FORMATTED:{code}")
    monkeypatch.setattr(processor_module, "print_analysis", lambda _: None)
    monkeypatch.setattr(processor_module, "print_plan", lambda _: None)
    monkeypatch.setattr(processor_module, "print_code", lambda _code, _lang: None)

    processor = CodeProcessor(llm=object())
    result_path = processor.process_file(str(input_file), output_path=str(output_file))

    assert result_path == str(output_file)
    assert output_file.read_text(encoding="utf-8") == "FORMATTED:print('ok')"


def test_format_fallback_returns_original_code_on_formatter_error(monkeypatch):
    monkeypatch.setattr(
        processor_module,
        "format_code",
        lambda _code, _language: (_ for _ in ()).throw(RuntimeError("formatter failed")),
    )

    processor = CodeProcessor(llm=object())
    raw = "print('no format')"
    assert processor._format(raw, "python") == raw
