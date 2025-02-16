from . import BaseAgent, BlogAgent, ExtendAgent, SummaryAgent
from prompts import PromptTemplate

class CmdAgent(BaseAgent):
    def create_post(self, instructions: str) -> str:
        """
        Create a new blog post according to instructions.
        
        Args:
          instructions: All instructions provided by the user.
          
        Returns:
          str: A success message with the contents of the newly created post.
        """
        post = self._interface._last_response = BlogAgent(username="Postcreator").chat(instructions)["content"]
        return f'Successfully generated a new post with the following content:\n{post}\n'

    def edit_post(self, instructions: str) -> str:
        """
        Edit the blog post according to instructions.
        
        Args:
          instructions: All instructions provided by the user.
          
        Returns:
          str: A success message with the contents of the edited post.
        """
        post = self._interface._last_response = ExtendAgent(self._interface._blog_post, username="Posteditor").chat(instructions)["content"]
        return f'Successfully edited the post and it now looks like:\n{post}\n'
    
    def summarize_post(self) -> str:
        """
        Create and add a summary to the blog post's metadata.
        
        Returns:
          str: A success message with the summary of the post.
        """
        summary = SummaryAgent().chat(self._interface._blog_post.join_content())["content"]
        self._interface._blog_post.update_summary(summary)
        return f'Successfully summarized the post and the summary is:\n{summary}\n'

    # TODO implement this as a tool
    def do_continue(self, arg):
        'Create a continuation blog post based on another post'
        args = arg.split()
        if len(args) < 1:
            print("you must provide a post name")
        base_post = BlogPost(args[0])
        self._last_response = ContinueAgent(blog_post=base_post, model=self._model).chat(arg)["content"]

    def get_sys(self):
        template_data=self._interface._blog_post.extract_metadata()
        return super().get_sys(template_data=template_data)

    def __init__(self, interface):
        super().__init__(PromptTemplate(prompt_file_name='cmd'), options={
            'num_ctx': 8*1024,
        })
        self._quiet = True
        self._interface = interface
        self.tools = [
            self.create_post,
            self.edit_post,
            self.summarize_post,
        ]