class PromptValidator:

    @staticmethod
    def validate_analysis(text: str):
        required = ["summary", "code smells", "solid"]
        lower = text.lower()

        if not all(r in lower for r in required):
            raise ValueError("Invalid analysis format")

    @staticmethod
    def validate_code(text: str):
        if "```" in text:
            raise ValueError("Code block formatting not allowed")