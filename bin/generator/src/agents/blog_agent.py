from app.history import History
from .base import BaseAgent

class BlogAgent(BaseAgent):
    def __init__(self, model: str, username: str = "Creating with instructions", history: History = History()):
        super().__init__(GeneratePrompt().generate(), model, username, history)