ANALYZE = """
You are a senior software engineer.

Language: {language}

Step 1: Analyze the code.

Return:
1. Summary
2. Issues
3. SOLID / best practices (if applicable)
4. Improvements list

Code:
{code}
"""


PLAN = """
Based on the improvements listed:

{analysis}

Return a structured refactoring plan.
"""


GENERATE = """
Refactor the code using this plan:

{plan}

Rules:
- Add type hints
- Add docstrings
- Keep behavior identical
- Return ONLY Python code
"""