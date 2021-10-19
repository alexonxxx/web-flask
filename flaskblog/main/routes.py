from flask import render_template, request, Blueprint
from flaskblog.models import Post

main=Blueprint('main',__name__)

# posts=[
# 	{
# 		'author': 'Alex Ballo',
# 		'title': 'Blog post 1',
# 		'content': 'First post content',
# 		'date_posted':'April 20, 2020'
# 	},
# 	{
# 		'author': 'Marc Rodriguez',
# 		'title': 'Blog post 2',
# 		'content': 'Second post content',
# 		'date_posted':'April 21, 2020'
# 	},{
# 		'title': 'Blog post 2',
# 		'content': 'Second post content',
# 		'date_posted':'April 21, 2020'
# 	}
# ]

@main.route("/")
@main.route("/home")
def home():
	page=request.args.get('page',1,type=int) #throws error if is not a number
	posts=Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=5)
	# posts=Post.query.all()	return render_template("home.html", posts=posts)
	return render_template("home.html", posts=posts)
@main.route("/about",methods=["GET"])
def about():
	return render_template("about.html",title="About")