from . import BaseAgent, BlogAgent, ExtendAgent, SummaryAgent

class CmdAgent(BaseAgent):
    def create_post(self, instructions: str) -> str:
        post = self._interface._last_response = BlogAgent().chat(instructions)["content"]
        return f'Successfully generated a new post with the following content:\n{post}\n'

    def edit_post(self, instructions: str) -> str:
        post = self._interface._last_response = ExtendAgent(self._interface._blog_post).chat(instructions)["content"]
        return f'Successfully edited the post and it now looks like:\n{post}\n'
    
    def summarize_post(self) -> str:
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
        
    def __init__(self, interface):
        super().__init__('You are a chat bot helping the user control a blog post generator application. You must use tools to interact with the application. After every tool call you must process the response and return it to the user.')
        self._interface = interface
        self.tools = [
            {
                'type': 'function',
                'function': {
                    'name': 'create_post',
                    'description': 'Create a new blog post according to instructions',
                    'parameters': {
                        'type': 'object',
                        'required': ['instructions'],
                        'properties': {
                            'instructions': {
                                'type': 'string',
                                'description': 'Instructions to create the post with'
                            },
                        },
                    },
                },
            }, {
                'type': 'function',
                'function': {
                    'name': 'edit_post',
                    'description': 'Edit the blog post according to instructions',
                    'parameters': {
                        'type': 'object',
                        'required': ['instructions'],
                        'properties': {
                            'instructions': {
                                'type': 'string',
                                'description': 'Instructions to edit the post with'
                            },
                        },
                    },
                },
            }, {
                'type': 'function',
                'function': {
                    'name': 'summarize_post',
                    'description': 'Create a summary of the blog post',
                },
            }
        ]