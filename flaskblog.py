from flask import Flask, render_template
from forms import RegistrationForm, LoginForm
app= Flask(__name__)

app.config["SECRET_KEY"]='18792050d1341be76feafb38979f40d4';

posts=[
	{
		'author': 'Alex Ballo',
		'title': 'Blog post 1',
		'content': 'First post content',
		'date_posted':'April 20, 2020'
	},
	{
		'author': 'Marc Rodriguez',
		'title': 'Blog post 2',
		'content': 'Second post content',
		'date_posted':'April 21, 2020'
	},{
		'title': 'Blog post 2',
		'content': 'Second post content',
		'date_posted':'April 21, 2020'
	}
]

@app.route("/")
@app.route("/home")
def hello():
	return render_template("home.html", posts=posts)

@app.route("/about",methods=["GET"])
def about():
	return render_template("about.html",title="About")

@app.route("/register")
def register():
	form= RegistrationForm()
	return render_template('register.html', title='Register', form=form)

@app.route("/login")
def register():
	form= LoginForm()
	return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80,debug=True)