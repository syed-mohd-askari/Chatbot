from flask import Flask, render_template, request
from model import qa_bot, final_result

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_query = request.form["query"]
        response = final_result(user_query)["result"] 
        return render_template("index.html", question=user_query, answer=response)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
