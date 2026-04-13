import os
import re

from security.sanitizer import sanitize
from security.file_validator import validate_file
from core.prompt_engine import PromptEngine
from core.language_detector import detect_language
from core.formatter import format_code
from ui.console import print_analysis, print_plan, print_code
from config.settings import OUTPUT_PREFIX, OUTPUT_DIR


class CodeProcessor:
    """
    Orchestrates the full code refactoring pipeline:
    validate → read → sanitize → analyze → plan → generate → format → persist
    """

    def __init__(self, llm):
        self._engine = PromptEngine(llm)


    def process_file(self, file_path: str, output_path: str | None = None) -> str:
        language = self._get_language(file_path)

        self._validate(file_path)
        code = self._load_file(file_path)
        code = self._sanitize(code, language)

        analysis = self._analyze(code, language)
        plan = self._plan(analysis, language)
        result = self._generate(plan, language)

        cleaned = self._clean_output(result)
        formatted = self._format(cleaned, language)

        final_path = self._resolve_output_path(file_path, output_path)
        self._save(final_path, formatted)

        self._render_output(analysis, plan, formatted, language)

        return final_path


    def _get_language(self, file_path: str) -> str:
        return detect_language(file_path)

    def _validate(self, file_path: str) -> None:
        validate_file(file_path)

    def _load_file(self, file_path: str) -> str:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    def _sanitize(self, code: str, language: str) -> str:
        return sanitize(code, language)

    def _analyze(self, code: str, language: str) -> str:
        analysis = self._engine.analyze(code, language)
        print_analysis(analysis)
        return analysis

    def _plan(self, analysis: str, language: str) -> str:
        plan = self._engine.plan(analysis, language)
        print_plan(plan)
        return plan

    def _generate(self, plan: str, language: str) -> str:
        return self._engine.generate(plan, language)

    def _format(self, code: str, language: str) -> str:
        try:
            return format_code(code, language)
        except Exception:
            return code


    def _resolve_output_path(self, file_path: str, override: str | None) -> str:
        if override:
            return override

        filename = os.path.basename(file_path)
        name, ext = os.path.splitext(filename)
        new_filename = f"{OUTPUT_PREFIX}_{name}{ext}"
        return os.path.join(OUTPUT_DIR, new_filename)

    def _save(self, path: str, content: str) -> None:
        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)


    @staticmethod
    def _clean_output(text: str) -> str:
        text = re.sub(r"```[a-zA-Z]*", "", text)
        return text.replace("```", "").strip()


    def _render_output(self, analysis: str, plan: str, code: str, language: str) -> None:
        print_code(code, language)