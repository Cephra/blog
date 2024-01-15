from blog_post import BlogPost
from prompt_template import PromptTemplate

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
        self._generate_template = PromptTemplate('generate.txt')
        self._summarize_template = PromptTemplate('summarize.txt')

    def generate_post(
                self,
                start_line: int = 0,
                end_line: int = None,
                skip_summary: bool = False,
                skip_generate: bool = False,
            ) -> str:
        if not skip_generate:
            # invoke ollama to generate post
            generate_prompt = self._generate_template.render(
                content=self._blog_post.join_content(start_line, end_line).strip(),
                instructions=self._instructions
            )
            generated_post = ollama.generate(
                model=self._model,
                prompt=generate_prompt,
            )
            self._blog_post.update_content(
                generated_post["response"],
                start_line, end_line
            )

        if not skip_summary:
            # invoke ollama to generate summary
            summarize_prompt = self._summarize_template.render(
                content=self._blog_post.join_content()
            )
            generated_summary = ollama.generate(
                model=self._model, 
                prompt=summarize_prompt
            )
            self._blog_post.update_summary(
                generated_summary["response"]
            )
        
        # save everything
        self._blog_post.save()