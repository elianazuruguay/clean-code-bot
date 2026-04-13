
from prompts.templates import GENERATE

class CodeGenerator:
    def __init__(self, llm):
        self.llm = llm

    def generate(self, plan):
        return self.llm.call(GENERATE.format(plan=plan))
