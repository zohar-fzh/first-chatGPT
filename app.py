import os
import openai
from flask import Flask, redirect, render_template, request, url_for

DEBUG=1

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    print("Hi, I am ChatGPT, a chatbot powered by OpenAI. How can I help you today?")
    if request.method == "POST":
        question = request.form["question"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=question.capitalize(),
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.6,
        )
        
        if DEBUG==True:
            print(question.capitalize())
            print(response.choices[0].text)
        
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)
