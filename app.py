import sys, os
from flask import Flask, render_template, url_for, request


STATIC_DIR = "static/imgs/"
app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def index(name="anon"):
    return render_template("index.html", name=name)

@app.route("/imgs/")
def imgs():
    print("##### In imgs method.", flush=True)
    page = request.args.get('page', 1, type=int)
    filenames = os.listdir(STATIC_DIR)
    num_images = len(filenames)
    filenames = filenames[(page - 1) * 100 : page * 100]
    last = (num_images - 1) // 100 + 1
    return render_template("imgs.html", filenames=filenames, page=page, last=last)

@app.route("/imgs/delete/", methods=["POST"])
def delete(fnames=[]):
    print("##### In delete method.", flush=True)
    if request.method == "POST":
        for fn in request.get_json(): 
            os.remove(STATIC_DIR + fn)
            print(f"## {fn} removed.   ", flush=True)
        print("\n## Finishing POST block, about to return from delete()...\n", flush=True)
    return f"<p>{request.get_json() if request.get_json() else 'Meeeeeuuuuuuuurrrrrggggghhhhhhhh!!!!!'}<\p>"

if __name__ == "__main__":
    app.run(debug=True)
