import cmd
from app.blog_post import BlogPost
from agents import *

class BlogGenerationInterface(cmd.Cmd):
    intro = 'Welcome to the AI-powered blog post generation interface!'
    
    def _prompt(self):
        return f"blog({self._postname})> "
    
    def __init__(self, *args, **kwargs):
        super().__init__()
        self._postname = kwargs["postname"]
        self._model = kwargs["model"]
        self._cmd_agent = CmdAgent(self)
        self.prompt = self._prompt()
        
    def precmd(self, line):
        self._blog_post = BlogPost(self._postname)
        return line
    
    def postcmd(self, stop, line):
        self._blog_post.update_content(
            self._last_response if hasattr(self, '_last_response') else self._blog_post.join_content()
        )
        if not stop:
            self._blog_post.save()
        return stop
        
    def do_bye(self, arg):
        'Exit the program'
        print('Bye!')
        return True
    
    def default(self, line):
        if line == 'EOF':
            return self.do_bye('')
        else:
            cmd_res = self._cmd_agent.chat(line)
            print(f'Assistant: {cmd_res.content}')
    
if __name__ == '__main__':
    BlogGenerationInterface().cmdloop()