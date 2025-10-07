listaEventos = []
proximo_id = 1

def validarData(dataStr):
    from datetime import datetime
    try:
        datetime.strptime(dataStr, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def adicionarEvento(listaEventos, nome, data, local, categoria):
    global proximo_id
    if not nome or not data or not local or not categoria:
        print("Erro: todos os campos devem ser preenchidos!\n")
        return
    if not validarData(data):
        print("Erro: data inválida! Use o formato AAAA-MM-DD\n")
        return
    evento = {"id": proximo_id, "nome": nome, "data": data, "local": local, "categoria": categoria}
    listaEventos.append(evento)
    proximo_id += 1
    print("Evento adicionado com sucesso!\n")

def listarEventos(listaEventos):
    if not listaEventos:
        print("Nenhum evento cadastrado.\n")
        return
    print("--- LISTA DE EVENTOS ---")
    for e in listaEventos:
        print(f"ID: {e['id']} | Nome: {e['nome']} | Data: {e['data']} | Local: {e['local']} | Categoria: {e['categoria']}")
    print()

def procurarEventoPorNome(listaEventos, nome):
    resultados = [e for e in listaEventos if nome.lower() in e["nome"].lower()]
    return resultados

def deletarEvento(listaEventos, id):
    for e in listaEventos:
        if e["id"] == id:
            listaEventos.remove(e)
            print("Evento deletado com sucesso!\n")
            return
    print("ID não encontrado!\n")

rodando = True
while rodando:
    print("=== Planejador de Eventos do IFB ===")
    print("1 - Adicionar Evento")
    print("2 - Listar Todos os Eventos")
    print("3 - Procurar Evento por Nome")
    print("4 - Deletar Evento por ID")
    print("5 - procurar por categoria")
    print("6 - Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        nome = input("Nome do evento: ")
        data = input("Data (AAAA-MM-DD): ")
        local = input("Local: ")
        categoria = input("Categoria: ")
        adicionarEvento(listaEventos, nome, data, local, categoria)
        
    elif escolha == "2":
        listarEventos(listaEventos)
        
    elif escolha == "3":
        nome = input("Digite o nome para buscar: ")
        resultados = procurarEventoPorNome(listaEventos, nome)
        if resultados:
            print("--- RESULTADOS ---")
            for e in resultados:
                print(f"ID: {e['id']} | Nome: {e['nome']} | Data: {e['data']} | Local: {e['local']} | Categoria: {e['categoria']}")
            print()
        else:
            print("Nenhum evento encontrado.\n")
    
    elif escolha == "4":
        id_str = input("Digite o ID do evento para deletar: ")
        if id_str.isdigit():
            deletarEvento(listaEventos, int(id_str))
        else:
            print("ID inválido!\n")
            
    elif escolha == "6":
        print("Saindo do sistema...")
        rodando = False
        
    else:
        print("Opção inválida!\n")