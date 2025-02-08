from .base import BaseAgent
from app.blog_post import BlogPost
from app.history import History
from app.prompts import ExtendPrompt

class ExtendAgent(BaseAgent):
    def __init__(self, blog_post: BlogPost, model: str, username: str = "Extending with instructions", history: History = History()):
        super().__init__(
            ExtendPrompt(
                blog_post.extract_metadata()
            ).generate(),
            model,
            username,
            history
        )
