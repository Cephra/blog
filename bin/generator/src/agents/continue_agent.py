"""Agent for drafting a follow-up post from an existing post."""

from . import BaseAgent
from app.blog_post import BlogPost
from prompts import PromptTemplate

class ContinueAgent(BaseAgent):
    def __init__(self, blog_post: BlogPost, *args, **kwargs):
        super().__init__(
            PromptTemplate(
                prompt_file_name='continue',
            ),
            *args,
            **kwargs
        )
        self._blog_post = blog_post

    def get_sys(self):
        template_data = self._blog_post.extract_metadata()
        return super().get_sys(template_data=template_data)
