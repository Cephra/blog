"""Agent for generating a new blog post from user instructions."""

from prompts import PromptTemplate
from . import BaseAgent

class BlogAgent(BaseAgent):
    def __init__(self, *args, **kwargs):
        super().__init__(PromptTemplate(prompt_file_name='generate'), *args, **kwargs)
