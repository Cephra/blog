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
        print(self._system_prompt)
        self._model = model
        self._username = username
        self._history = history
        self.tools = []
    
    def _handle_tools(self, response):
        for tool in response.message.tool_calls:
            result = None
            if hasattr(self, tool.function.name):
                tool_callable = getattr(self, tool.function.name)
                if callable(tool_callable):
                    args = tool.function.arguments
                    result = tool_callable(**args)
            self._history.push_tool(tool.function.name, result or "")
    
    def chat(self, prompt: str|None) -> str:
        if prompt is not None:
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
        self._history.push_message_obj(message.model_dump())
        
        if prompt is not None and response.message.tool_calls:
            print(response.message.tool_calls)
            self._handle_tools(response)
            print(self._history.get_with_sys(self._system_prompt))
            return self.chat(None)

        return message