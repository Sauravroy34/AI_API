from g4f.client import Client
from flask import Flask , request ,jsonify

app = Flask(__name__)


@app.route("/Ai/<text>")
def bot(text):

    client = Client()
    response = client.chat.completions.create(
        model="gemini",
        messages=[{"role": "user", "content": f"{text}"}],
        
    )
    data = (response.choices[0].message.content)
    return jsonify({"data":data})

# if __name__ == "__main__":
#     app.run(debug=True )