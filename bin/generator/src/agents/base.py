import ollama

from app.history import History

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