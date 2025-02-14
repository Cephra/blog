from . import BaseAgent
from prompts import PromptTemplate

class BlogAgent(BaseAgent):
    def __init__(self, *args, **kwargs):
        super().__init__(PromptTemplate(prompt_file_name='generate'), *args, **kwargs)