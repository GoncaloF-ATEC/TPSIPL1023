from flask import Flask, render_template, request, redirect

app = Flask(__name__)


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

lista_pessoas = [
    Pessoa("Gonçalo", 21),
    Pessoa("Maria", 21),
    Pessoa("Pedro", 21)
]



@app.route('/home')
def index():
    return render_template("home.html",
                           titulo="Home page",
                           nome="Gonçalo"
                           )
@app.route('/lista')
def infos():
    return render_template("lista.html",
                           pessoas=lista_pessoas)


@app.route('/infos/<usr_id>')
def infos2(usr_id: int):
    return f'Pagina de infos do {usr_id}'

# ?nome=Goncalo&idade=12
@app.route('/pag2/')
def pag2():

    nome = request.args.get('nome')
    idade = request.args.get('idade')
    return f'Pagina de infos do {nome}, com {idade} anos'

@app.route('/pag3/')
def pag3():
    return render_template("pag1.html")

@app.route('/pag4/')
def pag4():
    p = Pessoa("Gonçalo", 21)
    return render_template("pag2.html",
                           titulo="Pagina de infos",
                           pessoa=p)



@app.route('/add/')
def add_aluno():
    return render_template("add_alunos.html",
                           titulo="Adicionar aluno")



@app.post("/add_alunos")
def add_alunos():
    nome= request.form.get('nome')
    idade= request.form['idade']
    al = Pessoa(nome, idade)
    lista_pessoas.append(al)

    return redirect("/lista")





if __name__ == '__main__':
    app.run()

# flask run
