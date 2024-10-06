from flask import Flask, render_template
import requests

app = Flask(__name__)

url = "https://api.npoint.io/1faf7b2f02ff1c63fa24"
response = requests.get(url)
posts = response.json()

@app.route("/")
def home():
  return render_template("index.html", posts=posts)

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/contact")
def contact():
  return render_template("contact.html")

@app.route("/post/<int:number>")
def post(number):
  for post in posts:
    if post["id"] == number:
      return render_template("post.html", post=post)

if __name__ == "__main__":
  app.run(debug=True)