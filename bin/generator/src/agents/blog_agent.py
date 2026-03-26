"""Agent for generating a new blog post from user instructions."""

from app.retrieval import format_related_posts_context
from prompts import PromptTemplate
from . import BaseAgent

class BlogAgent(BaseAgent):
    def __init__(self, *args, **kwargs):
        super().__init__(PromptTemplate(prompt_file_name='generate'), *args, **kwargs)

    def get_sys(self, prompt: str = None):
        template_data = {}
        if prompt:
            template_data["related_posts_context"] = format_related_posts_context(prompt)
        return super().get_sys(template_data=template_data)
