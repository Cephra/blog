from app.history import History
import ollama

class BaseAgent():
    def __init__(
        self, 
        system_prompt: str,
        model: str = 'llama3.1',
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
        args = {
            "model": self._model, 
            "messages": self._history.get_with_sys(self._system_prompt),
        }

        # add tools if available in subclass
        if self.tools:
            args["tools"] = self.tools

        response = ollama.chat(**args)
        message = response['message']
        self._history.push_message_obj(message)
        return message