import openai
from flask import Flask, request, jsonify

app = Flask(__name__)
openai.api_key = "your-api-key-here"

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Скороти наступну статтю: {data['text']}",
        max_tokens=200
    )
    return jsonify({"summary": response["choices"][0]["text"].strip()})

if __name__ == '__main__':
    app.run(debug=True)
