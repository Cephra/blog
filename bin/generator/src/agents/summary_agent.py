from . import BaseAgent
from prompts import PromptTemplate

class SummaryAgent(BaseAgent):
    def __init__(self, *args, **kwargs):
        super().__init__(PromptTemplate(prompt_file_name='summary').generate(), *args, **kwargs)
        self._quiet = True