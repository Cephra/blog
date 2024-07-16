from blog_post import BlogPost
from prompt_template import PromptTemplate
from history import History
from agents import BlogAgent, ExtendAgent, SummaryAgent

import ollama

class BlogPostGenerator:
    def __init__(
                self,
                postname: str,
                instructions: str,
                model: str = 'llama3'
            ) -> None:
        self._model = model

        self._postname = postname
        self._instructions = instructions

        self._blog_post = BlogPost(postname)
        self._history = History()
        self._generate_agent = BlogAgent(model=model, history=self._history)
        self._extend_agent = ExtendAgent(blog_post=self._blog_post, model=model, history=self._history)
        self._summary_agent = SummaryAgent(model=model)

    def generate_post(
                self,
                instructions: str,
                start_line: int = 0,
                end_line: int = None,
                skip_summary: bool = False,
                skip_generate: bool = False,
            ) -> str:
        if self._blog_post.is_fresh:
            self._generate_agent.chat(instructions)
        else:
            self._extend_agent.chat(instructions)

        last_response = self._history.get_last()
        self._blog_post.update_content(
            last_response,
            start_line=start_line,
            end_line=end_line
        )
        
        summary = self._summary_agent.chat(self._blog_post.join_content(
            start_line=start_line,
            end_line=end_line
        ))["content"]
        self._blog_post.update_summary(summary)

        # save everything
        self._blog_post.save()
        
    def repl(self):
        while True:
            instructions = input('User: ')
            self.generate_post(instructions)