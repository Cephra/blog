import ollama

class BaseAgent():
    def __init__(self, system_prompt: str, model: str):
        self._system_prompt = system_prompt
        self._model = model
        self._history = []
    
    def _sys_with_history(self) -> str:
        return [ {
            'role': 'system',
            'content': self._system_prompt
        } ] + self._history
    
    def chat(self, prompt: str) -> str:
        print("Human: ", prompt)
        messages = self._sys_with_history() + [ {
            'role': 'user',
            'content': prompt
        } ]
        response = ollama.chat(model=self._model, messages=messages)
        message = response['message']
        self._history.append(message)
        return message

if __name__ == '__main__':
    agent = BaseAgent(system_prompt="You are a helpful assistant.", model="llama3")
    print(agent.chat("Tell me a joke."))
    print(agent.chat("Now that was funny!"))