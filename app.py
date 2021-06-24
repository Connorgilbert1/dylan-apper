from flask import Flask, render_template, request, url_for, redirect
from sql import SQL

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello world!'


@app.route('/post/<int:post_id>')  # /post/0
def post(post_id):
    # if file_exists("posts.json"):
    #     with open("posts.json", "r", encoding="utf-8") as fp:
    #         post = json.load(fp)[str(post_id)]
    # else:
    #     post = False

    post = SQL().load(post_id)

    if not post:  # post will be None if not found; not None => True
        return render_template('404.html', message=f'A post with id {post_id} was not found.')
    return render_template('post.html', post=post)


@app.route('/post/form')
def form():
    return render_template('create.html')


@app.route('/post/create', methods=['POST'])
def create():
    title = request.form.get('title')
    content = request.form.get('content')

    post_id = SQL().save(title, content)

    return redirect(url_for('post', post_id=post_id))


if __name__ == "__main__":
    from waitress import serve
    print("running app")
    serve(app, host="0.0.0.0", port=80)

