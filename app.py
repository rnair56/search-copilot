from flask import Flask, render_template, request, jsonify
# import openai
from copilot.calling_agents_setup import user_proxy, manager
from utils import parse_chat_entries

app = Flask(__name__)

# Replace 'your_api_key' with your actual OpenAI API key
# openai.api_key = 'your_api_key'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json['message']
    chat_response = user_proxy.initiate_chat(
    manager,message= user_message)
    # message="Find a latest paper about gpt-4 on arxiv and find its potential applications in software."
    response_message = parse_chat_entries(chat_response.chat_history)
    return jsonify({"response": response_message})
    return None

if __name__ == "__main__":
    app.run(debug=True)
