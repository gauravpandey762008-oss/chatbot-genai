from flask import Flask, render_template, request, jsonify
from ai import ask_ai

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    history = request.json["history"]          # pichli saari baatein (memory)
    prompt = "You are a friendly assistant. Reply in simple words.\n"
    for m in history:
        prompt += f"{m['role']}: {m['text']}\n"
    prompt += "bot:"
    return jsonify(reply=ask_ai(prompt))

app.run(debug=True)
