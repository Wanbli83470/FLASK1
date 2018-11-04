from flask import Flask, render_template
# from mocks import Post
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/apso.sqlite3'
db = SQLAlchemy(app)

app = Flask(__name__)

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    content = db.Column(db.String(255), unique=True, nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.username

@app.context_processor
def inject_now():
	return {'now': datetime.now()}

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/contact")
def contact():
	return render_template("contact.html")

@app.route("/blog")
def blog():
	posts = Post.all()
	return render_template("posts/blog.html" , posts = posts)

@app.route("/blog/posts/<int:id>")
def posts(id):
	post = Post.find(id)
	print(id)
	return render_template("posts/show.html" , post = post)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

if __name__ == "__main__" :
	db.create_all()
	app.run(debug = True)