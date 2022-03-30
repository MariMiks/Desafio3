from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("index.html")

@app.route('/quem-somos')
def quemSomos():
    return render_template("Quem_somos.html")

@app.route('/contatos')
def contato():
    return render_template("Contato.html")

if __name__ == "__main__":
    app.run(debug=True)