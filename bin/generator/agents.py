import ollama

from history import History

from blog_post import BlogPost

from prompts import *

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
    
class BlogAgent(BaseAgent):
    def __init__(self, model: str, username: str = "Creating with instructions", history: History = History()):
        super().__init__(GeneratePrompt().generate(), model, username, history)

class ExtendAgent(BaseAgent):
    def __init__(self, blog_post: BlogPost, model: str, username: str = "Extending with instructions", history: History = History()):
        super().__init__(
            ExtendPrompt(
                blog_post.extract_metadata()
            ).generate(),
            model,
            username,
            history
        )

class ContinueAgent(BaseAgent):
    def __init__(self, blog_post: BlogPost, model: str, username: str = "Continuing with instructions", history: History = History()):
        super().__init__(
            ContinuePrompt(
                blog_post.extract_metadata()
            ).generate(),
            model,
            username,
            history
        )

class SummaryAgent(BaseAgent):
    def __init__(self, model: str, username: str = "Summarizing", history: History = History()):
        super().__init__(SummarizePrompt().generate(), model, username, history)
