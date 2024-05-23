from agents import BaseAgent

class BlogAgent(BaseAgent):
    system_prompt = """
    You are a blog post skeleton agent. You will be given a topic and create a rough structure for the blog post.
    You will use headers such as # for headings, ## for subheadings, ### for sub-subheadings, etc.
    You will only return markdown code for the blog post.
    You must not return any other text.
    You must not output anything but the headings.
    You must end at the same heading level that you started at.
    You have to come to a conclusion at the end.
    """
    def __init__(self, model="llama3"):
        super().__init__(self.system_prompt, model)

    def create_post(self, topic: str):
        prompt = "Write a blog post on \"{topic}\"."
        return self.chat(prompt.format(topic=topic))

if __name__ == '__main__':
    agent = BlogAgent()
    print(agent.create_post('The city of Berlin, Germany')['content'])
