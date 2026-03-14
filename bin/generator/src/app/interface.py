"""Interactive command loop for generating and editing blog posts."""

import cmd
import sys
from app.blog_post import BlogPost
from agents import *

class BlogGenerationInterface(cmd.Cmd):
    intro = 'Welcome to the AI-powered blog post generation interface!'

    def _prompt(self):
        return f"blog({self._postname})> "

    @property
    def blog_post(self) -> BlogPost:
        if self._blog_post is None:
            raise RuntimeError("No blog post is loaded.")
        return self._blog_post

    @property
    def model(self) -> str:
        return self._model

    def __init__(self, *args, **kwargs):
        super().__init__()
        self._postname = kwargs["postname"]
        self._model = kwargs["model"]
        self._cmd_agent = CmdAgent(self)
        self.prompt = self._prompt()
        self._blog_post = None

    def precmd(self, line):
        self._blog_post = BlogPost(self._postname)
        return line

    def set_last_response(self, response: str) -> str:
        self._last_response = response
        return response

    def postcmd(self, stop, line):
        self.blog_post.update_content(
            self._last_response if hasattr(self, '_last_response') else self.blog_post.join_content()
        )
        if not stop:
            self.blog_post.save()
        return stop

    def do_dbg(self, arg):
        'Print debug'
        print(self._cmd_agent)

    def do_bye(self, arg):
        'Exit the program'
        print('Bye!')
        return True

    def default(self, line):
        if line == 'EOF':
            return self.do_bye('')
        else:
            try:
                cmd_res = self._cmd_agent.chat(line)
                print(f'Assistant: {cmd_res.content}')
            except ConnectionError:
                print('There was a problem talking to ollama. Exiting...', file=sys.stderr)
                sys.exit(1)
    
if __name__ == '__main__':
    BlogGenerationInterface().cmdloop()
