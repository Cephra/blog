class History():
    def __init__(self):
        self._history: list = []
    
    def get_with_sys(self, sys_prompt: str):
        return [ {
            'role': 'system',
            'content': sys_prompt
        } ] + self._history

    def push_message_obj(self, message: dict):
        self._history.append(message)
        
    def push_message(self, role: str, message: str):
        self.push_message_obj({
            'role': role,
            'content': message
        })
        
    def push_tool(self, tool: str, output: str):
        self.push_message_obj({
            'role': 'tool',
            'content': output,
            'name': tool
        })
        
    def get_last(self) -> str:
        return self._history[-1]