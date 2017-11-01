from flask import Flask, escape, render_template, session
import random
app = Flask (__name__)

@app.route ('/')
def compliment_andrew():
	return 'hello, beautiful!'


@app.route('/number_please')
def number_please():
	return "{}". format(random.randint(1,20))


# @app.route('/<name>')
# def compliment_abdul(name):
# 	return "hello, beautiful {}!".format(escape(name))


@app.route('/<name>')
def compliment_abdul(name):
	return render_template("hello.html", name=name)


@app.route('/compliment/<name>/<int:number>')
def compliment(name,number):
	return render_template("hello.html", name=name , number=number)


@app.route('/welcome/<name>')
def welcome(name):
	if not 'is_andrew' in session:
		session['is_andrew'] = name.title() == "Andrew"  #title allows acceptance of any kinds of cases, it automatically just set the first case to a Title case

	return  render_template("welcome.html", is_andrew=session['is_andrew'])

@app.route('/logout')
def logout():
	session.clear()
	return "logged.out. Try again"

#SLIDE 18 from the flask slide

@app.route('/secret/<password>')
def confirm_password(password):
	if not 'is_loggedin' in session:
		session['is_loggedin'] =password="bananaPie"

	return render_template("welcome.html", is_loggedin=session['is_loggedin'])

@app.route('/session')
def 



app.secret_key = b'4.\xc9\xbd\x8e\xd2\x9b\xad\xca\x99\x8f\xd4\xbda`\xf1\xb4\x92U\x8e\xb5\x85\xbd\xf7'

if __name__ == '__main__':
	app.run()

