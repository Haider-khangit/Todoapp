from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(app)


class Users(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(10), nullable=False)
    desc = db.Column(db.String(100), nullable=False)
    
    def __repr__(self) -> str:
        return f"{self.title} - {self.desc}"


@app.route('/', methods=["GET", "POST"])
def Helloworld():
    if request.method == "POST":
        title = request.form["title"]
        desc = request.form["desc"]
        todo = Users(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
    
    alltodo = Users.query.all()
    return render_template('index.html', alltodo=alltodo)


@app.route('/delete/', methods=['POST'])
def delete_todo(Sno):
    todo = Users.query.get_or_404(Sno)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True, port=8000)