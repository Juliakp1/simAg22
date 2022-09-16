from ast import Return
from src.model.quadronegro import *
import pytest

d = Disciplina("DevLife")
tur = Turma(d, "DevLife 2022/1")
estudante = Estudante("Diana Deana")
estudante.matricular(tur)
tarefa = Tarefa(tur, "Pedro Álvares Cabral")
tur.tarefas.append(tarefa)
resp = ['A', 'C', 'B']
sub = Submissao(tarefa, resp)


@pytest.mark.sim_ag22
def test_verificar_se_submissoes_possuem_texto_no_atributo_resposta():
    assert sub.resposta == resp


@pytest.mark.sim_ag22
def test_verificar_se_submissoes_do_estudante_sao_de_tarefas_de_turmas_do_estudante():
    for item in tarefa.submissoes:
        if (item in tur.tarefas) and (estudante not in tur.estudantes):
            assert False
    assert True
 

@pytest.mark.sim_ag22
def test_verificar_se_estudante_pertence_a_uma_turma():
    jaCadastrado = False
    for turma in Turma.allTurmas:
        if estudante in turma.estudantes:
            if jaCadastrado:
                assert False
            jaCadastrado = True
    assert True



@pytest.mark.sim_ag22
def test_verificar_se_todas_as_turmas_do_estudante_sao_do_ano_atual():
    for turma in Turma.allTurmas:
        if turma.estudantes.count(estudante) > 1:
            assert False
    assert True

