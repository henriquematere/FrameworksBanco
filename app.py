from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Nullable

app = Flask(__name__)
app.config ["SAQLALCHEMY_DATABASE_URI"]="sqlite:///pessoas.db"

db = SQLAlchemy(app)
class Pessoa:
    def __init__(self,nome,sobrenome,cpf,email,telefone):
        self.id = db.Column(db.Integer,primary_key=True)
        self.nome = db.Column(db.String(100),Nullable)
        self.sobrenome = db.Column(db.String(100),Nullable)
        self.cpf = db.Column(db.String(100),Nullable)
        self.email = db.Column(db.String(100),Nullable)
        self.telefone = db.Column(db.Integer(100), Nullable)

@app.route('/')
def formulario():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, port=2000)