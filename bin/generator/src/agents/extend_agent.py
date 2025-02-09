from . import BaseAgent
from app.blog_post import BlogPost
from app.history import History
from prompts import ExtendPrompt

class ExtendAgent(BaseAgent):
    def __init__(self, blog_post: BlogPost, *args, **kwargs):
        super().__init__(
            ExtendPrompt(
                blog_post.extract_metadata()
            ).generate(),
            *args, **kwargs
        )
