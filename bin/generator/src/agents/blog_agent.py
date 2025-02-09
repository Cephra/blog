from . import BaseAgent
from app.history import History
from prompts import GeneratePrompt

class BlogAgent(BaseAgent):
    def __init__(self, *args, **kwargs):
        super().__init__(GeneratePrompt().generate(), *args, **kwargs)