from . import BaseAgent
from app.history import History
from prompts import SummarizePrompt

class SummaryAgent(BaseAgent):
    def __init__(self, *args, **kwargs):
        super().__init__(SummarizePrompt().generate(), *args, **kwargs)