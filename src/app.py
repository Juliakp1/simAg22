from flask import Flask, request, jsonify
from pathlib import Path
import pandas as pd
from model.quadronegro import *


app = Flask(__name__)

@app.before_first_request
def executa_antes_do_primeiro_request():
    pass
    
# --------------------------------------------------- #

@app.route("/")
def hello_world():
    return "<p>Hello, Prova AG22!</p>"

# --------------------------------------------------- #

@app.route("/tarefas/all/")
def listar_tarefas():
    """Deve retornar uma lista com o nome de todas as tarefas"""
    lista = ['Todas as tarefas']
    todasTarefas = FachadaTarefa.listar_tarefas()
    for item in todasTarefas:
        lista.append(str(item))
    print(lista)
    return jsonify(lista)

# --------------------------------------------------- #

@app.route("/tarefas/<string:nome_tarefa>/<string:nome_estudante>/")
def listar_notas_estudante(nome_tarefa:str, nome_estudante:str):
    """Deve retornar uma lista com as notas que o estudante obteve em todas as suas submissões para uma dada tarefa"""
    lista = ['Notas que o estudante obteve em todas as suas submissões para uma dada tarefa']
    todasTarefas = FachadaTarefa.listar_notas_estudante(nome_tarefa, nome_estudante)
    for item in todasTarefas:
        lista.append(str(item))
    print(lista)
    return jsonify(lista)

# --------------------------------------------------- #

@app.route("/disciplinas/<string:nome_estudante>/")
def listar_disciplinas(nome_estudante:str):
    lista = ['Todas as disciplinas do estudante']
    todasTarefas = FachadaTarefa.listar_disciplinas(nome_estudante)
    for item in todasTarefas:
        lista.append(str(item))
    print(lista)
    return jsonify(lista)

# --------------------------------------------------- #

@app.route("/add_all/")
def creates_light_database():
    d = Disciplina("DevLife")
    tur = Turma(d, "DevLife 2022/1")
    estudante = Estudante("Diana Deana")
    estudante.matricular(tur)
    tarefa = Tarefa(tur, "Pedro Álvares Cabral")
    tur.tarefas.append(tarefa)
    resp = ['A', 'C', 'B']
    sub = Submissao(tarefa, resp)
    tarefa.submeter(resp, estudante)
    return jsonify('Added!')

# --------------------------------------------------- #

if __name__ == '__main__':
    app.run(debug=True)