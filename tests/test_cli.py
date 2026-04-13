from click.testing import CliRunner

import cli as cli_module
from security.file_validator import FileValidationError


class FakeProcessor:
    def __init__(self, llm):
        self.llm = llm

    def process_file(self, file, output_path=None):
        return output_path or f"output/{file}"


def test_cli_success_path(monkeypatch):
    messages = {"success": None, "error": None}

    monkeypatch.setattr(cli_module, "OpenAIClient", lambda: object())
    monkeypatch.setattr(cli_module, "CodeProcessor", FakeProcessor)
    monkeypatch.setattr(cli_module, "print_success", lambda msg: messages.__setitem__("success", msg))
    monkeypatch.setattr(cli_module, "print_error", lambda title, msg: messages.__setitem__("error", (title, msg)))

    runner = CliRunner()
    result = runner.invoke(cli_module.main, ["input.py", "--output", "custom.py"])

    assert result.exit_code == 0
    assert messages["success"] == "Saved output to custom.py"
    assert messages["error"] is None


def test_cli_handles_file_validation_error(monkeypatch):
    messages = {"success": None, "error": None}

    class FileErrorProcessor:
        def __init__(self, llm):
            self.llm = llm

        def process_file(self, file, output_path=None):
            raise FileValidationError("bad file")

    monkeypatch.setattr(cli_module, "OpenAIClient", lambda: object())
    monkeypatch.setattr(cli_module, "CodeProcessor", FileErrorProcessor)
    monkeypatch.setattr(cli_module, "print_success", lambda msg: messages.__setitem__("success", msg))
    monkeypatch.setattr(cli_module, "print_error", lambda title, msg: messages.__setitem__("error", (title, msg)))

    runner = CliRunner()
    result = runner.invoke(cli_module.main, ["missing.py"])

    assert result.exit_code == 0
    assert messages["success"] is None
    assert messages["error"] == ("File Validation Error", "bad file")


def test_cli_handles_unexpected_error(monkeypatch):
    messages = {"success": None, "error": None}

    class BoomProcessor:
        def __init__(self, llm):
            self.llm = llm

        def process_file(self, file, output_path=None):
            raise RuntimeError("boom")

    monkeypatch.setattr(cli_module, "OpenAIClient", lambda: object())
    monkeypatch.setattr(cli_module, "CodeProcessor", BoomProcessor)
    monkeypatch.setattr(cli_module, "print_success", lambda msg: messages.__setitem__("success", msg))
    monkeypatch.setattr(cli_module, "print_error", lambda title, msg: messages.__setitem__("error", (title, msg)))

    runner = CliRunner()
    result = runner.invoke(cli_module.main, ["input.py"])

    assert result.exit_code == 0
    assert messages["success"] is None
    assert messages["error"] == ("Unexpected Error", "boom")
