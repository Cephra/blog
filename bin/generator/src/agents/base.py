from app.history import History
from prompts import PromptTemplate
import ollama

class BaseAgent():
    def __str__(self):
        return str(self.get_sys())
        return str(self._history)

    def __init__(
        self, 
        system_prompt: str|PromptTemplate,
        model: str = 'llama3.1',
        username: str = "User",
        options: dict = None,
        history: History = None
    ):
        self._system_prompt = system_prompt
        self._model = model
        self._username = username
        self._quiet = False
        self._history = History() if history is None else history
        self._options = {} if options is None else options 
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
            
    def _validate_message(self, message, tool_message) -> bool:
        if tool_message:
            return True if len(message.content) > 0 else False
        else:
            if message.tool_calls:
                available_tools = [tool["function"]["name"] for tool in self.tools]
                for call in message.tool_calls:
                    if call.function.name not in available_tools:
                        return False
                return True
            elif len(message.content) == 0:
                return False
            else:
                return True
            
    def get_sys(self, *args, **kwargs):
        if isinstance(self._system_prompt, PromptTemplate):
            return self._system_prompt.generate(*args, **kwargs)
        else:
            return self._system_prompt
    
    def chat(self, prompt: str|None) -> str:
        if prompt is not None:
            if not self._quiet:
                print("{}: {}".format(self._username, prompt))
            self._history.push_message("user", prompt)

        args = {
            "model": self._model, 
            "messages": self._history.get_with_sys(self.get_sys()),
        }
        # add options if available in subclass
        if self._options:
            args["options"] = self._options
        # add tools if available in subclass
        if self.tools:
            args["tools"] = self.tools
            
        message = None
        message_valid = False
        while not message_valid:
            response = ollama.chat(**args)
            message = response.message
            message_valid = self._validate_message(message, True if not prompt else False)
        self._history.push_message_obj(message.model_dump())
        
        if prompt is not None and response.message.tool_calls:
            self._handle_tools(response)
            return self.chat(None)

        return message