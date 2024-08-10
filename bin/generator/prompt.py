from jinja2 import Template

# Used to generate prompts for the agent
class PromptTemplate():
    def __init__(self):
        self._template_data = dict()
        # TODO allow multiple prompts (eg. array of prompt files) or maybe Jinja can do it
        with open("./prompts/{}.txt".format(prompt_file_name)) as f:
            template_body = f.read()
            self._template = Template(template_body)
    
    def generate(self):
        return self._template.render()

# Used to generate a new blog post
class GeneratePrompt(PromptTemplate):
    pass

# Used to extend an existing blog post
class ExtendPrompt(PromptTemplate):
    pass

# Used to summarize a new blog post
class SummarizePrompt(PromptTemplate):
    pass

# Used to continue an existing blog post
class ContinuePrompt(PromptTemplate):
    pass