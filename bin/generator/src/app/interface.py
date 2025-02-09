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
    
    def do_summarize(self, arg):
        'Generate a blog post summary'
        summary = SummaryAgent(model=self._model).chat(self._blog_post.join_content())["content"]
        self._blog_post.update_summary(summary)

    def do_continue(self, arg):
        'Create a continuation blog post based on another post'
        args = arg.split()
        if len(args) < 1:
            print("you must provide a post name")
        base_post = BlogPost(args[0])
        self._last_response = ContinueAgent(blog_post=base_post, model=self._model).chat(arg)["content"]

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
            print(cmd_res)
    
if __name__ == '__main__':
    BlogGenerationInterface().cmdloop()