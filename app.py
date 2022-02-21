import os
from flask import Flask, render_template, url_for, request


app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def index(name="anon"):
    return render_template("index.html", name=name)

@app.route("/imgs/")
def imgs():
    page = request.args.get('page', 1, type=int)
    filenames = os.listdir("static/imgs/")
    num_images = len(filenames)
    filenames = filenames[(page - 1) * 100 : page * 100]
    last = (num_images - 1) // 100 + 1
    return render_template("imgs.html", filenames=filenames, page=page, last=last)

if __name__ == "__main__":
    app.run(debug=True)
