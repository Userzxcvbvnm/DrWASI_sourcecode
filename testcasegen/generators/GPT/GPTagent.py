from openai import OpenAI 


class GPTAgent:
    def __init__(self):
        self.client = OpenAI()

    def request(self, reqstr):
        res = ""
        stream = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": reqstr}],
            stream=True,
        )       
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                res += chunk.choices[0].delta.content
        return res

