from flask import Flask, render_template
app = Flask(__name__)


@app.route('/inex')
def index(name=None):
    return render_template("indix.html", name=name)


@app.route('/product')
def product():
    return "THsi is the product page"    


if __name__ == "__main__":
    app.run(debug=True, port=5000)


