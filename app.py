from flask import Flask, render_template, request, jsonify
# import openai

app = Flask(__name__)

# Replace 'your_api_key' with your actual OpenAI API key
# openai.api_key = 'your_api_key'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    # user_message = request.json['message']
    # # Call the OpenAI API with the user's message
    # response = openai.Completion.create(
    #   engine="text-davinci-003", # Update the engine if needed
    #   prompt=user_message,
    #   temperature=0.7,
    #   max_tokens=150,
    #   top_p=1.0,
    #   frequency_penalty=0.0,
    #   presence_penalty=0.0
    # )
    # response_message = response.choices[0].text.strip()
    # return jsonify({"response": response_message})
    return None

if __name__ == "__main__":
    app.run(debug=True)
