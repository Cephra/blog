from . import BaseAgent
from app.blog_post import BlogPost
from prompts import ContinuePrompt

class ContinueAgent(BaseAgent):
    def __init__(self, blog_post: BlogPost, *args, **kwargs):
        super().__init__(
            ContinuePrompt(
                blog_post.extract_metadata()
            ).generate(),
            *args,
            **kwargs
        )