import os
from aluno import repository as aluno_repository


alunos = []
tamanho_da_tela = 100
comando_limpar_tela = "clear"

def imprimirSeparador(char = "-"):
    print(char*tamanho_da_tela)

def imprimirCabecalho(cabecalho):
    imprimirSeparador("=")
    print(f"||{cabecalho:^{tamanho_da_tela-4}}||")
    imprimirSeparador("=")


def cadastrarAluno():
    imprimirCabecalho("Cadastrar aluno")
    
    nome = input("Digite o nome do aluno: ")
    turma = int(input("Digite a turma do aluno: "))
    notas = []
    qtd_faltas = 0
    
    aluno = {
        "nome": nome,
        "turma": turma,
        "notas": notas,
        "faltas": qtd_faltas
    }

    try:
        aluno_repository.insert_aluno(aluno)
    except Exception as e:
        print(e)
    


def listarAlunos():
    imprimirCabecalho("Lista de alunos")

    alunos = aluno_repository.select_alunos()
    ids = []

    if alunos:
        for aluno in alunos:
            print(formataTextoTamanhoTela(f"Aluno {aluno["id"]} | {aluno['nome']}"))
            ids.append(aluno["id"])
            imprimirSeparador()
    else:
        print("Não há alunos cadastrados")
    
    return ids

def mostrarFaltasAluno(aluno):
    print(f"{aluno['nome']} possui {aluno['faltas']} faltas.")

def escolherOpcaoMenuPaginaDoAluno(aluno):
    listaOpcoes = [
        {"opcao": "1", "descricao": "Editar nome", "funcao": editarNomeAluno},
        {"opcao": "2", "descricao": "Editar turma", "funcao": editarTurmaAluno},
        {"opcao": "3", "descricao": "Adicionar nota", "funcao": adicionarNotaAluno},
        {"opcao": "4", "descricao": "Adicionar falta", "funcao": adicionarFaltaAluno},
        {"opcao": "5", "descricao": "Mostrar média", "funcao": mostrarMediaAluno},
        {"opcao": "6", "descricao": "Mostrar notas", "funcao": mostrarNotasAluno},
        {"opcao": "7", "descricao": "Mostrar faltas", "funcao": mostrarFaltasAluno},
        {"opcao": "v", "descricao": "Voltar", "funcao": None}
    ]

    return selecionarOpcao(listaOpcoes, f"Aluno: {aluno['nome']} - Turma: {aluno['turma']}")


def editarNomeAluno(aluno):
    novo_nome = input("Digite o novo nome do aluno: ")
    aluno_repository.update_nome_aluno(aluno['id'], novo_nome)

def editarTurmaAluno(aluno):
    nova_turma = int(input("Digite a nova turma do aluno: "))
    aluno_repository.update_turma_aluno(aluno['id'], nova_turma)

def adicionarNotaAluno(aluno):
    nova_nota = float(input("Digite a nova nota do aluno: "))
    aluno_repository.insert_nota_aluno(aluno['id'], nova_nota)

def adicionarFaltaAluno(aluno):
    qtd_faltas_para_Adicionar = int(input("Digite a quantidade de faltas a serem adicionadas: "))
    aluno_repository.insert_falta_aluno(aluno['id'], qtd_faltas_para_Adicionar)

def mostrarMediaAluno(aluno):
    if len(aluno['notas']) == 0:
        print("O aluno ainda não possui notas cadastradas")
    else:
        media = sum(aluno['notas']) / len(aluno['notas'])
        print(f"A média do aluno é {media}")
    

def mostrarNotasAluno(aluno):
    os.system(comando_limpar_tela)
    if len(aluno['notas']) == 0:
        print("O aluno ainda não possui notas cadastradas")
    else:
        imprimirCabecalho(f"Notas do aluno: {aluno['nome']}")
        for i in range(len(aluno['notas'])):
            nota = aluno['notas'][i]
            print(f"Nota {i} | {nota}")
            imprimirSeparador()



def paginaDoAluno():
    imprimirCabecalho("Acesso a página do aluno")
    ids = listarAlunos()

    if ids:
        indice = int(input("Para acessar a página do aluno digite o índice: "))
        while indice not in ids:
            print("Índice inválido")
            indice = int(input("Para acessar a página do aluno digite o índice: "))

        
        while True:
            os.system(comando_limpar_tela)
            aluno = aluno_repository.select_aluno(indice)
            if aluno:
                opcao = escolherOpcaoMenuPaginaDoAluno(aluno)
                
                if opcao["funcao"]:
                    opcao["funcao"](aluno)
                else:
                    break
                input("Pressione Enter para continuar...")
            else:
                print("Aluno não encontrado!")
                input("Pressione Enter para continuar...")
                break

def removerAluno():
    imprimirCabecalho("Remover aluno")
    ids = listarAlunos()
    indice = input("Digite o índice do aluno que deseja remover: ")

    if indice in ids:
        aluno_repository.delete_aluno(indice)
    else:
      print("Índice inválido")
        

def formataTextoTamanhoTela(texto):
    return f'|| {texto:{tamanho_da_tela - 5}}||'


def selecionarOpcao(listaOpcoes, cabecalho):
    while True:
        imprimirCabecalho(cabecalho)
        for op in listaOpcoes:
            print(formataTextoTamanhoTela(f"{op['opcao']} - {op['descricao']}"))
        imprimirSeparador("=")

        opcao = input("Digite a opção desejada: ")
        for op in listaOpcoes:
            if op['opcao'] == opcao:
                return op
        print("Opção inválida!")
        input("Pressione Enter para continuar...")
        os.system(comando_limpar_tela)


def escolherOpcaoMenuPrincipal():
    
    listaOpcoes = [
        {"opcao": "1", "descricao": "Cadastrar aluno", "funcao": cadastrarAluno},
        {"opcao": "2", "descricao": "Listar alunos", "funcao": listarAlunos},
        {"opcao": "3", "descricao": "Página do aluno", "funcao": paginaDoAluno},
        {"opcao": "4", "descricao": "Remover aluno", "funcao": removerAluno},
        {"opcao": "5", "descricao": "Sair", "funcao": None}
    ]

    return selecionarOpcao(listaOpcoes, "Sistema de alunos")


def main():
    
    while True:
        os.system(comando_limpar_tela)
        opcao = escolherOpcaoMenuPrincipal()
        os.system(comando_limpar_tela)
        if opcao["funcao"]:
            opcao["funcao"]()
        else:
            break

        input("Pressione Enter para continuar...")
    print("Obrigado por usar o sistema de alunos!")

main()