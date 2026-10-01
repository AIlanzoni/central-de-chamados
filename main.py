def criar_chamado(id_chamado):
    name = input("Digite o nome do solicitante: ")
    descricao = input("Digite a descrição do chamado: ")
    categoria = input("Digite a categoria do chamado: ")
    prioridade = input("Digite a prioridade do chamado (Alta, Média, Baixa): ")
    
    while categoria not in ['Hardware', 'Software', 'Rede', 'Acesso', 'Suporte']:
        print("Categoria inválida!")
        categoria = input("Digite a categoria novamente: ")
    
    while prioridade not in ['Alta', 'Média', 'Baixa']:
        print("Prioridade inválida!")
        prioridade = input("Digite a prioridade novamente: ")
           
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

def buscar_chamados(chamados):
    id_chamado = int(input("Digite o ID do chamado que deseja buscar: "))
    
    for chamado in chamados:
        if chamado['id'] == id_chamado:
            return chamado

    print("Chamado não encontrado!")

def atualizar_status(chamados):
    id_chamado = int(input("Digite o ID do chamado que deseja buscar: "))
    
    for chamado in chamados:
        if chamado['id'] == id_chamado:
            novo_status = input("Digite o novo status do chamado (Aberto, Em andamento, Concluído): ")
            
            while novo_status not in ['Aberto', 'Em andamento', 'Concluído']:
                print("Status inválido!")
                novo_status = input("Digite o novo status do chamado novamente: ")
            
            chamado['status'] = novo_status
            return chamado
    
    print("Chamado não encontrado!")
        
def alterar_prioridade(chamados):
    id_chamado = int(input("Digite o ID do chamado que deseja buscar: "))
    
    for chamado in chamados:
        if chamado['id'] == id_chamado:
            nova_prioridade = input("Digite a nova prioridade do chamado (Alta, Média, Baixa): ")
            
            while nova_prioridade not in ['Alta', 'Média', 'Baixa']:
                print("Prioridade inválida!")
                nova_prioridade = input("Digite a nova prioridade do chamado novamente: ")
            
            chamado['prioridade'] = nova_prioridade
            return chamado
        
    print("Chamado não encontrado!")
            
chamados = []
adicionar_chamado(chamados)
adicionar_chamado(chamados)
listar_chamados(chamados)
print(buscar_chamados(chamados))
print(atualizar_status(chamados))
print(alterar_prioridade(chamados))
print("Chamados adicionados com sucesso!")