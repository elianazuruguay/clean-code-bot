
from abc import ABC, abstractmethod

class LLMProvider(ABC):
    @abstractmethod
    def call(self, prompt: str) -> str:
        pass
