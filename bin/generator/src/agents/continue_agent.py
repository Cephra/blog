from app.history import History

from app.blog_post import BlogPost

from .base import BaseAgent

from app.prompts import ContinuePrompt

class ContinueAgent(BaseAgent):
    def __init__(self, blog_post: BlogPost, model: str, username: str = "Continuing with instructions", history: History = History()):
        super().__init__(
            ContinuePrompt(
                blog_post.extract_metadata()
            ).generate(),
            model,
            username,
            history
        )