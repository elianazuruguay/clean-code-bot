from prompts.templates import ANALYZE, PLAN, GENERATE


class PromptEngine:

    def __init__(self, llm):
        self.llm = llm

    def analyze(self, code: str, language: str) -> str:
        prompt = ANALYZE.format(
            code=code,
            language=language
        )
        return self.llm.call(prompt)

    def plan(self, analysis: str, language: str) -> str:
        prompt = PLAN.format(
            analysis=analysis,
            language=language
        )
        return self.llm.call(prompt)

    def generate(self, plan: str, language: str) -> str:
        prompt = GENERATE.format(
            plan=plan,
            language=language
        )
        return self.llm.call(prompt)