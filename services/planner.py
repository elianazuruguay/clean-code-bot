
from prompts.templates import PLAN

class RefactorPlanner:
    def __init__(self, llm):
        self.llm = llm

    def plan(self, analysis):
        return self.llm.call(PLAN.format(analysis=analysis))
