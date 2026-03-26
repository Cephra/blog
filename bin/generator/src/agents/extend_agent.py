"""Agent for revising an existing blog post."""

from . import BaseAgent
from app.blog_post import BlogPost
from app.retrieval import format_related_posts_context
from prompts import PromptTemplate

class ExtendAgent(BaseAgent):
    def __init__(self, blog_post: BlogPost, *args, **kwargs):
        super().__init__(
            PromptTemplate(
                prompt_file_name='extend',
            ),
            *args, **kwargs
        )
        self._blog_post = blog_post
    
    def get_sys(self, prompt: str = None):
        template_data=self._blog_post.extract_metadata()
        if prompt:
            template_data["related_posts_context"] = format_related_posts_context(
                prompt,
                current_post_slug=self._blog_post.slug,
            )
        return super().get_sys(template_data=template_data)
