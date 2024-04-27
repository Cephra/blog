#!/usr/bin/env python3

import sys
import os
import subprocess

from string import Template

script_dir = os.path.dirname(__file__)

class BlogPost:
    def __init__(self, postname: str) -> None:
        self._postname = postname
        self._postfile = os.path.join(script_dir, '../content/posts', self._postname + '.md')

        self._front_matter = []
        self._content = []

        if not os.path.exists(self._postfile):
            cmd = ['hugo', 'new', 'content', 'posts/{0}.md'.format(self._postname)]
            subprocess.run(cmd, check=True, cwd=os.path.join(script_dir, '..'))
        self.read_post()

    def read_post(self) -> None:
        try:
            with open(self._postfile, 'r') as file:
                is_front_matter = False

                for line in file:
                    if line.startswith('+++'):
                        is_front_matter = not is_front_matter
                        self._front_matter.append(line)
                        continue

                    if is_front_matter:
                        self._front_matter.append(line)
                    else:
                        self._content.append(line)
        except FileNotFoundError as e:
            print(f"Error: File '{self._postfile}' not found.")
        except IOError as e:
            print(f"Error reading file '{self._postfile}': {e}")

    def join_content(self) -> str:
        return "".join(self._content)

    def join_front_matter(self) -> str:
        return "".join(self._front_matter)
    
    def update_content(self, new_content: str) -> None:
        self._content = ["{}\n".format(line) for line in new_content.split('\n')]
    
    def update_summary(self, new_summary: str) -> None:
        new_front_matter = [line for line in self._front_matter if not line.startswith('summary')]
        new_front_matter.insert(-1, "{}\n".format(new_summary.strip()))
        self._front_matter = new_front_matter

    def save(self) -> None:
        with open(self._postfile, 'w') as file:
            if self._front_matter:
                file.write(self.join_front_matter())
            if self._content:
                file.write(self.join_content())

class PromptTemplate:
    def __init__(self, template_file: str) -> None:
        filename = os.path.join(script_dir, 'prompts', template_file)
        self._template = Template(open(filename, 'r').read())

    def render(self, **kwargs) -> str:
        return self._template.substitute(**kwargs)

class BlogPostGenerator:
    def __init__(self, postname: str, instructions: str = '') -> None:
        self._postname = postname
        self._instructions = instructions

        self._blog_post = BlogPost(postname)
        self._generate_template = PromptTemplate('generate.txt')
        self._summarize_template = PromptTemplate('summarize.txt')

    def generate_post(self) -> str:
        joined_content = self._blog_post.join_content()

        # invoke ollama to generate post
        generate_prompt = self._generate_template.render(
            content=self._blog_post.join_content(),
            instructions=self._instructions
        )
        ollama_post = subprocess.Popen(['ollama', 'run', 'llama3'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        generated_post = ollama_post.communicate(generate_prompt.encode('utf-8'))[0].decode('utf-8')
        self._blog_post.update_content(generated_post)

        # invoke ollama to generate summary
        summarize_prompt = self._summarize_template.render(
            content=self._blog_post.join_content()
        )
        ollama_summary = subprocess.Popen(['ollama', 'run', 'llama3'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        generated_summary = ollama_summary.communicate(summarize_prompt.encode('utf-8'))[0].decode('utf-8')
        self._blog_post.update_summary(generated_summary)
        
        # save everything
        self._blog_post.save()

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc != 3:
        print("Usage: python script.py <postname> <instructions>") 
        sys.exit(1)

    blog_post_generator = BlogPostGenerator(
        sys.argv[1],
        sys.argv[2]
    )
    blog_post_generator.generate_post()