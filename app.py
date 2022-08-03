from flask import Flask,render_template,url_for,request
import requests

url = ("https://api.npoint.io/43644ec4f0013682fc0d")
posts = requests.get(url)
posts.raise_for_status()
posts.json()


app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/contact.html")
def contact():
    success=''
    return render_template("contact.html", success=success)

@app.route('/login', methods=["POST"])
def receive_data():
    data = request.form
    print(data["name"])
    print(data["email"])
    print(data["phone"])
    print(data["message"])
    return render_template("contact.html", success="successfully sent message")

# @app.route('/post<int:id>')
# def post(id):
#     ind = id - 1
#     display_post = posts[ind]
#     return render_template("post.html", display_post=display_post)



# @app.route("/post<int:id>")
@app.route("/post.html")
def post():
    return render_template("post.html")
# def post(id):
#     ind = id-1
#     display_post = posts[ind]
#     return render_template("post.html", display_post=display_post)
# def show_post(index):
#     requested_post=None
#     for blog_post in posts:
#         if blog_post["id"] == index:
#             requested_post=blog_post
#     return render_template("post.html", post=requested_post)






if __name__ == "__main__" :
    app.run(debug=True, port=7878)