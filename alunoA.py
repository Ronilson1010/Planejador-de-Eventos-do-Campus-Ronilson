listaEventos = []
proximo_id = 1

def validarData(data):
    from datetime import datetime
    try:
        datetime.strptime(data, "%Y-%m-%d")
        return True
    except:
        return False

def adicionarEvento(lista, nome, data, local, categoria):
    global proximo_id
    if nome == "" or data == "" or local == "" or categoria == "":
        print("Erro: preencha todos os campos")
        return
    if not validarData(data):
        print("Erro: data invalida")
        return
    evento = {
        "id": proximo_id,
        "nome": nome,
        "data": data,
        "local": local,
        "categoria": categoria,
        "participado": False
    }
    lista.append(evento)
    proximo_id += 1
    print("Evento adicionado!")

def listarEventos(lista):
    if len(lista) == 0:
        print("Nenhum evento")
        return
    print("Lista de eventos:")
    for e in lista:
        print("ID:", e["id"], "| Nome:", e["nome"], "| Data:", e["data"], "| Local:", e["local"], "| Categoria:", e["categoria"])

def procurarEventoPorNome(lista, nome):
    resultados = []
    for e in lista:
        if nome.lower() in e["nome"].lower():
            resultados.append(e)
    return resultados

def deletarEvento(lista, id):
    for e in lista:
        if e["id"] == id:
            lista.remove(e)
            print("Evento deletado")
            return
    print("ID nao encontrado")

def displayMenu():
    print("\n=== Menu ===")
    print("1 - Adicionar evento")
    print("2 - Listar eventos")
    print("3 - Procurar evento")
    print("4 - Deletar evento")
    print("5 - Filtrar categoria (em breve)")
    print("6 - Marcar participacao (em breve)")
    print("7 - Relatorio (em breve)")
    print("8 - Sair")

def getEscolhaDoUsuario():
    escolha = input("Escolha uma opcao: ")
    if escolha.isdigit():
        return int(escolha)
    return 0

rodando = True
while rodando:
    displayMenu()
    escolha = getEscolhaDoUsuario()

    if escolha == 1:
        nome = input("Nome do evento: ")
        data = input("Data AAAA-MM-DD: ")
        local = input("Local: ")
        categoria = input("Categoria: ")
        adicionarEvento(listaEventos, nome, data, local, categoria)

    elif escolha == 2:
        listarEventos(listaEventos)

    elif escolha == 3:
        achados = procurarEventoPorNome(listaEventos, nome=input("Digite o nome: "))
        if len(achados) == 0:
            print("Nenhum encontrado")
        else:
            for e in achados:
                print("ID:", e["id"], "| Nome:", e["nome"], "| Data:", e["data"], "| Local:", e["local"], "| Categoria:", e["categoria"])

    elif escolha == 4:
        id_str = input("ID do evento: ")
        if id_str.isdigit():
            deletarEvento(listaEventos, int(id_str))
        else:
            print("ID invalido")

    elif escolha == 8:
        print("Saindo...")
        rodando = False

    else:
        print("Opcao invalida ou ainda nao implementada")
