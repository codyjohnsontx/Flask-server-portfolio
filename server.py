from flask import Flask, render_template, url_for
import os
app = Flask(__name__)

print(__name__)


@app.route("/<username>/<int:post_id>")
def hello_world(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)

@app.route('/about')
def about():
    return render_template('about.html')


"""
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

                              """ 


@app.route('/blogs/2020/dogs')
def blog2():
    return 'WOOF WOOF MY DUDE'