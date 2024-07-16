import ollama

from history import History

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

if __name__ == '__main__':
    agent1 = BaseAgent(system_prompt="You're Dave, a right wing person with extreme views on political opinions. You're talking to Max, who is a left wing person with extreme views on politics. You do not agree with Max and want to convince him of your views.", model="llama3", username="Max")
    agent2 = BaseAgent(system_prompt="You're Max, a left wing person with extreme views on political opinions. You're talking to Dave, who is a right wing person with extreme views on politics. You do not agree with Dave. You try not to let Dave's opinion on you.", model="llama3", username="Dave")
    agent_resp = agent1.chat('Hey Dave, how are you? It\'s me, Max!')
    user_resp = agent2.chat(agent_resp['content'])
    for i in range(3):
        agent_resp = agent1.chat(user_resp['content'])
        user_resp = agent2.chat(agent_resp['content'])
    response = agent1.chat(user_resp['content'])
    print("{}: {}".format(agent2._username, response['content']))