from datetime import date

from jinja2 import Environment, FileSystemLoader

path = "prompts"
template_env = Environment(loader=FileSystemLoader(path))

# Used to generate prompts for the agent
class PromptTemplate():
    def __init__(self, prompt_file_name: str, template_data: dict = dict()):
        self._template_data = template_data
        self._template_data["date"] = date.today().strftime("%A %B %d, %Y")
        self._template = template_env.get_template("{}.txt".format(prompt_file_name))
        self._debug = False
    
    def generate(self):
        rendered_prompt = self._template.render(self._template_data)
        if self._debug:
            print(rendered_prompt)
        return rendered_prompt

# Used to generate a new blog post
class GeneratePrompt(PromptTemplate):
    def __init__(self, template_data: dict = dict()):
        super().__init__("generate", template_data)

# Used to extend an existing blog post
class ExtendPrompt(PromptTemplate):
    def __init__(self, template_data: dict = dict()):
        super().__init__("extend", template_data)

# Used to summarize a new blog post
class SummarizePrompt(PromptTemplate):
    def __init__(self, template_data: dict = dict()):
        super().__init__("summarize", template_data)

# Used to continue an existing blog post
class ContinuePrompt(PromptTemplate):
    def __init__(self, template_data: dict = dict()):
        super().__init__("continue", template_data)
