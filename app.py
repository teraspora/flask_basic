from flask import Flask, redirect, render_template, request, url_for, session

app = Flask(__name__)

@app.route("/<name>")
def index(name="anon"):
    return render_template("index.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)