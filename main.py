def criar_chamado(id_chamado):
    name = input("Digite o nome do solicitante: ")
    descricao = input("Digite a descrição do chamado: ")
    categoria = input("Digite a categoria do chamado: ")
    prioridade = input("Digite a prioridade do chamado (Alta, Média, Baixa): ")
    
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