from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>" \
        "Guess a number between 0 and 9" \
        "<h1 />" \
        '<iframe src="https://giphy.com/embed/sTczweWUTxLqg" width="480" height="346" style="" frameBorder="0" class="giphy-embed"></iframe>'

def generate_answer():
    return random.randint(1,9)

@app.route("/<int:guess_number>")
def guess(guess_number):
    if guess_number < answer:
        return "<h1 style = 'color: red'>" \
            "Too low, try again!" \
            "<h1 />"
    elif guess_number > answer:
        return "<h1 style = 'color: purple'>" \
            "Too high, try again!" \
            "<h1 />"
    else:
        return "<h1 style = 'color: green'>" \
            "You found me!" \
            "<h1 />"


answer = generate_answer()

if __name__ == "__main__":
    app.run(debug=True)
    