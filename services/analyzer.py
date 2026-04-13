
from prompts.templates import ANALYZE

class CodeAnalyzer:
    def __init__(self, llm):
        self.llm = llm

    def analyze(self, code):
        return self.llm.call(ANALYZE.format(code=code))
