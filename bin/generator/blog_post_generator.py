from blog_post import BlogPost
from prompt_template import PromptTemplate
from agents import BlogAgent, ExtendAgent, SummaryAgent

import ollama

class BlogPostGenerator:
    def __init__(
                self,
                postname: str,
                model: str = 'llama3'
            ) -> None:
        self._model = model
        self._postname = postname

    def generate_post(
                self,
                instructions: str,
                start_line: int = 0,
                end_line: int = None,
                skip_summary: bool = False,
                skip_generate: bool = False,
            ) -> str:
        self._blog_post = BlogPost(self._postname)

        agent = None
        last_response = None

        if self._blog_post.is_fresh:
            agent = BlogAgent(model=self._model)
        else:
            agent = ExtendAgent(blog_post=self._blog_post, model=self._model)

        last_response = agent.chat(instructions)["content"]

        self._blog_post.update_content(
            last_response,
            start_line=start_line,
            end_line=end_line
        )
        
        summary_agent = SummaryAgent(model=self._model)
        summary = summary_agent.chat(self._blog_post.join_content(
            start_line=start_line,
            end_line=end_line
        ))["content"]
        self._blog_post.update_summary(summary)

        # save everything
        self._blog_post.save()
        
    def repl(self):
        while True:
            try:
                instructions = input('User: ')
                self.generate_post(instructions)
            except:
                print("Bye!")
                break