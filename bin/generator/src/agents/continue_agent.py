from . import BaseAgent
from app.blog_post import BlogPost
from app.history import History
from prompts import ContinuePrompt

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