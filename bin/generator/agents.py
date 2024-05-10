import ollama

class BaseAgent():
    def __init__(self, system_prompt: str, model: str, usernick: str):
        self._system_prompt = system_prompt
        self._model = model
        self._usernick = usernick
        self._history = []
    
    def _sys_with_history(self) -> str:
        return [ {
            'role': 'system',
            'content': self._system_prompt
        } ] + self._history
    
    def chat(self, prompt: str) -> str:
        print("\n# {}\n{}\n".format(self._usernick, prompt))
        messages = self._sys_with_history() + [ {
            'role': 'user',
            'content': prompt
        } ]
        response = ollama.chat(model=self._model, messages=messages)
        message = response['message']
        self._history.append(message)
        return message

if __name__ == '__main__':
    agent1 = BaseAgent(system_prompt="You're dave talking to your friend max. Introduce yourself. Be curious, ask questions.", model="llama3", usernick="Max")
    agent2 = BaseAgent(system_prompt="You're max talking to your friend dave. Introduce yourself. Be curious, ask questions.", model="llama3", usernick="Dave")
    agent_resp = agent1.chat('Hey Dave, how are you?')
    user_resp = agent2.chat(agent_resp['content'])
    for i in range(10):
        agent_resp = agent1.chat(user_resp['content'])
        user_resp = agent2.chat(agent_resp['content'])
    agent1.chat(user_resp['content'])