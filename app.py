from flask import Flask, render_template


app = Flask(__name__, static_url_path = "/static", static_folder = "static")


@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/results')
def results():
	return render_template('results.html')

if __name__ == '__main__':
	app.run(debug=True)