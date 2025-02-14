from datetime import date

from jinja2 import Environment, FileSystemLoader

import os
path = "src/prompts/templates"
template_env = Environment(loader=FileSystemLoader(path))

# Used to generate prompts for the agent
class PromptTemplate():
    def __init__(self, prompt_file_name: str):
        self._template = template_env.get_template("{}.txt".format(prompt_file_name))
        self._debug = False
    
    def generate(self, template_data: dict = None):
        template_data = {} if template_data is None else template_data
        template_data["date"] = date.today().strftime("%A %B %d, %Y")
        rendered_prompt = self._template.render(template_data)
        if self._debug:
            print(rendered_prompt)
        return rendered_prompt

if __name__ == "__main__":
    pass