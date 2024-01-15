import os

from string import Template

class PromptTemplate:
    def __init__(self, template_file: str) -> None:
        filename = os.path.join('prompts', template_file)
        self._template = Template(open(filename, 'r').read())

    def render(self, **kwargs) -> str:
        return self._template.substitute(**kwargs)