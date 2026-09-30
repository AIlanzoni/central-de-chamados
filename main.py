def criar_chamado(id_chamado):
    name = input("Digite o nome do solicitante: ")
    descricao = input("Digite a descrição do chamado: ")
    categoria = input("Digite a categoria do chamado: ")
    prioridade = input("Digite a prioridade do chamado (Alta, Média, Baixa): ")
    
    if categoria not in ['Hardware', 'Software', 'Rede', 'Acesso', 'Suporte']:
        print("Categoria inválida. Definindo como 'Software'.")
        categoria = 'Software'
    
    if prioridade not in ['Alta', 'Média', 'Baixa']:
        print("Prioridade inválida. Definindo como 'Baixa'.")
        prioridade = 'Baixa'
    
    chamado = {
        'id': id_chamado,
        'nome': name,
        'descricao': descricao,
        'categoria': categoria,
        'prioridade': prioridade,
        'status': 'Aberto'
    }
    
    return chamado

def adicionar_chamado(chamados):
    chamado = criar_chamado(id_chamado=len(chamados) + 1)
    chamados.append(chamado)
    
    return chamados

def listar_chamados(chamados):
    
    for chamado in chamados:
        print(f"ID: {chamado['id']}, Nome: {chamado['nome']}, Descrição: {chamado['descricao']}, Categoria: {chamado['categoria']}, Prioridade: {chamado['prioridade']}, Status: {chamado['status']}")
        
chamados = []
adicionar_chamado(chamados)
adicionar_chamado(chamados)
listar_chamados(chamados)
print("Chamados adicionados com sucesso!")