import ollama

class BaseAgent():
    def __init__(self, system_prompt: str, model: str, username: str = "User"):
        self._system_prompt = system_prompt
        self._model = model
        self._username = username
        self._history = []
    
    def _sys_with_history(self) -> str:
        return [ {
            'role': 'system',
            'content': self._system_prompt
        } ] + self._history
    
    def chat(self, prompt: str) -> str:
        print("{}: {}".format(self._username, prompt))
        self._history.append({
            'role': 'user',
            'content': prompt
        })
        response = ollama.chat(model=self._model, messages=self._sys_with_history())
        message = response['message']
        self._history.append(message)
        return message

if __name__ == '__main__':
    agent1 = BaseAgent(system_prompt="You're dave, an it security specialist talking to your coworker Max. You are both analyzing the origin of an attack on your systems. Try your best to solve it.", model="llama3", username="Max")
    agent2 = BaseAgent(system_prompt="You're dave, an it security specialist talking to your coworker Dave. You are both analyzing the origin of an attack on your systems. Try your best to solve it.", model="llama3", username="Dave")
    agent_resp = agent1.chat('Hey Dave, how are you? It\'s me, Max!')
    user_resp = agent2.chat(agent_resp['content'])
    for i in range(3):
        agent_resp = agent1.chat(user_resp['content'])
        user_resp = agent2.chat(agent_resp['content'])
    response = agent1.chat(user_resp['content'])
    print("{}: {}".format(agent2._username, response['content']))