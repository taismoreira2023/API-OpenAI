import os
from flask import Flask, request, render_template, jsonify
from openai import OpenAI
from helpers import carrega
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = 'alura'

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

contexto = carrega("dados/ecormat.txt")
# print("CONTEXT CARREGADO:\n", contexto)
def assistente_simples(mensagem):
    prompt_do_sistema = f"""
            {contexto}
            """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": prompt_do_sistema
                },
            {
                "role": "user", 
                "content": mensagem
                }
        ]
    )
    return response.choices[0].message.content

@app.route("/chat", methods=["POST"])
def chat():
    prompt = request.json.get("msg", "")
    resposta = assistente_simples(prompt)
    
    return jsonify({"resposta": resposta})

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
