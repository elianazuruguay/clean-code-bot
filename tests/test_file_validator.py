import pytest

from security.file_validator import FileValidationError, validate_file


def test_validate_file_accepts_supported_extension(tmp_path):
    file_path = tmp_path / "sample.py"
    file_path.write_text("print('ok')", encoding="utf-8")

    assert validate_file(str(file_path)) is True


def test_validate_file_raises_when_file_missing(tmp_path):
    missing = tmp_path / "missing.py"

    with pytest.raises(FileValidationError, match="File not found"):
        validate_file(str(missing))


def test_validate_file_raises_for_unsupported_extension(tmp_path):
    file_path = tmp_path / "notes.txt"
    file_path.write_text("hello", encoding="utf-8")

    with pytest.raises(FileValidationError, match="not supported"):
        validate_file(str(file_path))
