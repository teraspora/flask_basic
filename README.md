The basic structure for a dockerised Flask app.

`$ docker build --tag fs .`

`$ docker run  --rm -p 5002:5000 -v $(pwd):/app fs`

Go to http://127.0.0.1:5002/ in a browser.
Change stuff and refresh.