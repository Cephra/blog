import ollama

from history import History

from blog_post import BlogPost

class BaseAgent():
    def __init__(
        self, 
        system_prompt: str,
        model: str,
        username: str = "User",
        history: History = History()
    ):
        self._system_prompt = system_prompt
        self._model = model
        self._username = username
        self._history = history
    
    def chat(self, prompt: str) -> str:
        print("{}: {}".format(self._username, prompt))
        self._history.push_message("user", prompt)
        response = ollama.chat(
            model=self._model,
            messages=self._history.get_with_sys(self._system_prompt)
        )
        message = response['message']
        self._history.push_message_obj(message)
        return message
    
class PromptFileAgent(BaseAgent):
    def __init__(self, prompt_file_name: str, model: str, username: str = "User", history: History = History()):
        with open("./prompts/{}.txt".format(prompt_file_name)) as f:
            super().__init__("".join(f.readlines()), model, username, history)
    
class BlogAgent(PromptFileAgent):
    def __init__(self, model: str, username: str = "Creating with instructions", history: History = History()):
        super().__init__("generate", model, username, history)

class ExtendAgent(PromptFileAgent):
    def __init__(self, blog_post: BlogPost, model: str, username: str = "Extending with instructions", history: History = History()):
        super().__init__("extend", model, username, history)
        self._system_prompt += blog_post.join_content()

class SummaryAgent(PromptFileAgent):
    def __init__(self, model: str, username: str = "Summarizing", history: History = History()):
        super().__init__("summarize", model, username, history)