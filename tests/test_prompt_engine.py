from core.prompt_engine import PromptEngine


class FakeLLM:
    def __init__(self):
        self.prompts = []

    def call(self, prompt: str) -> str:
        self.prompts.append(prompt)
        return "ok"


def test_prompt_engine_builds_prompts_with_language_and_inputs():
    llm = FakeLLM()
    engine = PromptEngine(llm)

    assert engine.analyze("print('hi')", "python") == "ok"
    assert engine.plan("analysis data", "python") == "ok"
    assert engine.generate("plan data", "python") == "ok"

    assert "Language: python" in llm.prompts[0]
    assert "print('hi')" in llm.prompts[0]
    assert "analysis data" in llm.prompts[1]
    assert "plan data" in llm.prompts[2]
