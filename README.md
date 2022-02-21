The basic structure for a dockerised Flask app, now with some added functionality, to display paginated screens of images from a directory on the server - so docker run and map a volume as below.

`$ docker build --tag fs .`

`$ docker run  --rm -p 5002:5000 -v $(pwd):/app -v <directory containing png images>:/app/static/imgs fs`

Go to http://127.0.0.1:5002/imgs/ in a browser.