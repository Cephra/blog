from . import BaseAgent
from app.blog_post import BlogPost
from prompts import PromptTemplate

class ContinueAgent(BaseAgent):
    def __init__(self, blog_post: BlogPost, *args, **kwargs):
        super().__init__(
            ContinuePrompt(
                prompt_file_name='continue',
                template_data=blog_post.extract_metadata()
            ).generate(),
            *args,
            **kwargs
        )