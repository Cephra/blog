from . import BaseAgent, BlogAgent, ExtendAgent

class CmdAgent(BaseAgent):
    def create_post(self, instructions: str) -> str:
        post = BlogAgent().chat(instructions)["content"]
        return f'Successfully generated the following post:\n{post}\n'

    def edit_post(self, instructions: str) -> str:
        post = ExtendAgent(self._interface._blog_post).chat(instructions)["content"]
        return f'Successfully edited the post and it now looks like:\n{post}\n'
        
    def __init__(self, interface):
        super().__init__('You are a chat bot helping the user control a blog post generator application. You must use tools to interact with the application. After every tool call you must process the response and return it to the user.', options={
            'temperature': 0,
        })
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
                    'description': 'Add a summary of a blog post',
                },
            }
        ]