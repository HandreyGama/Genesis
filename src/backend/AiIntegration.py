import requests
import os
from dotenv import load_dotenv

load_dotenv()

class Ai():
    def __init__(self):
        self.API_KEY = os.getenv("GENESIS_AI_API_KEY");
        self.URL = "https://api.groq.com/openai/v1/chat/completions"
        self.headers = {"Authorization":f"Bearer {self.API_KEY}"}

    def PerguntarChat(self,planeta):
        prompt = f"""Descreva em poucas palavras o exoplaneta:{planeta},
        falando do raio,temperatura,gravidade,
        como foi descoberto,quem descobriu,aonde descobriram,se possivel deixe essa parte mais detalhada do que as outras
        as outras podem ser mais curtas,artigos cientificos se tiver relacionados a ele,noticias, e em que localização ele se encontra,
        caso não ache uma das informaçõesa,
        apenas não mencione nada,ou seja NÃO ESCREVA NADA NA SUA RESPOSTA,somente diga as informações que encontrou """
        model_data = {
            "model": "llama-3.1-8b-instant",
            "messages": [{"role": "user", "content": prompt}]
        }
        r = requests.post(self.URL,json=model_data,headers=self.headers)
        return r.json()["choices"][0]["message"]["content"]

ai = Ai()
print(ai.PerguntarChat("TRAPPIST-1e"))