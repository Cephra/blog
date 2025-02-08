from . import BaseAgent
from app.history import History
from app.prompts import SummarizePrompt

class SummaryAgent(BaseAgent):
    def __init__(self, model: str, username: str = "Summarizing", history: History = History()):
        super().__init__(SummarizePrompt().generate(), model, username, history)