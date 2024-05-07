import ollama

import sys

system_prompt = """
You're a robot writing or extending blog posts in Markdown.

You reply with only the newly created or extended blog post.

You must include any shortcodes present in the original post.
Shortcodes look like this: {{< shortcode [args] >}}

You include the original content of the blog post.
"""

if __name__ == "__main__":
    with open("mnt-workspace/content/posts/{}".format(sys.argv[1])) as f:
        content = f.read()
        messages = [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "assistant",
                "content": "Hello, please provide instructions for creating or extending a blog post:"
            },
            {
                "role": "user",
                "content": "Write about how information from webpages could be included in blogposts. Don't change the original post."
            },
            {
                "role": "assistant",
                "content": "Sure, give me the content of the post please:"
            },
            {
                "role": "user",
                "content": content,
            },
        ]
        response = ollama.chat('llama3', messages=messages)
        print(response["message"]["content"])
