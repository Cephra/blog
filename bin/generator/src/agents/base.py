from app.history import History
import ollama

class BaseAgent():
    def __init__(
        self, 
        system_prompt: str,
        model: str = 'llama3.1',
        username: str = "User",
        options: dict = {},
        history: History = History()
    ):
        self._system_prompt = system_prompt
        self._model = model
        self._username = username
        self._quiet = False
        self._history = history
        self._options = options
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
            if not self._quiet:
                print("{}: {}".format(self._username, prompt))
            self._history.push_message("user", prompt)

        args = {
            "model": self._model, 
            "messages": self._history.get_with_sys(self._system_prompt),
        }
        # add options if available in subclass
        if self._options:
            args["options"] = self._options
        # add tools if available in subclass
        if self.tools:
            args["tools"] = self.tools
            
        message = None
        while True:
            response = ollama.chat(**args)
            message = response['message']
            if prompt is not None or len(message.content) > 0:
                break
        self._history.push_message_obj(message.model_dump())
        
        if prompt is not None and response.message.tool_calls:
            self._handle_tools(response)
            return self.chat(None)

        return message