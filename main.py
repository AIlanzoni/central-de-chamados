import random

def main():
    while True:
        print('\n===== CENTRAL DE CHAMADOS =====')
        print('1. Adicionar chamado')
        print('2. Listar chamados')
        print('3. Buscar chamado')
        print('4. Atualizar status do chamado')
        print('5. Alterar prioridade do chamado')
        print('6. Remover chamado')
        print('7. Filtrar status dos chamados')
        print('0. Sair')
        try:
            opcao = int(input('\nEscolha uma opção: '))
            
            if opcao == 1:
                adicionar_chamado(chamados)
            elif opcao == 2:
                listar_chamados(chamados)
            elif opcao == 3:
                print(buscar_chamados(chamados))
            elif opcao == 4:
                print(atualizar_status(chamados))
            elif opcao == 5:
                print(alterar_prioridade(chamados))
            elif opcao == 6:
                remover_chamado(chamados)
            elif opcao == 7:
                filtrar_por_status(chamados)
            elif opcao == 0:
                print('Saindo do sistema...')
                break
            else:
                print('Opção inválida! Tente novamente.')
        except ValueError:
            print('Digite apenas números!')

def criar_chamado(id_chamado):
    name = input("Digite o nome do solicitante: ").strip().lower()
    descricao = input("Digite a descrição do chamado: ").strip().lower()
    categoria = input("Digite a categoria do chamado: ").strip().lower()
    prioridade = input("Digite a prioridade do chamado (Alta, Média, Baixa): ").strip().lower()
    
    while categoria not in ['hardware', 'software', 'rede', 'acesso', 'suporte']:
        print("Categoria inválida!")
        categoria = input("Digite a categoria novamente: ").strip().lower()
    
    while prioridade not in ['alta', 'média', 'baixa']:
        print("Prioridade inválida!")
        prioridade = input("Digite a prioridade novamente: ").strip().lower()
           
    chamado = {
        'id': id_chamado,
        'nome': name,
        'descricao': descricao,
        'categoria': categoria,
        'prioridade': prioridade,
        'status': 'aberto'
    }
    
    return chamado

def adicionar_chamado(chamados):
    
    id_chamado = random.randint(1, 1000)
    
    for chamado in chamados:
        if chamado['id'] == id_chamado:
            print(f"Chamado já existe!")
        
    while True:
        
        id_existe = False
        
        for chamado in chamados:
            if chamado['id'] == id_chamado:
                id_existe = True

        if id_existe:
            id_chamado = random.randint(1, 1000)
        else:
            break
            
    chamado = criar_chamado(id_chamado=id_chamado)
    chamados.append(chamado)
    
    return chamados

def listar_chamados(chamados):
    
    for chamado in chamados:
        print(f"ID: {chamado['id']}, Nome: {chamado['nome']}, Descrição: {chamado['descricao']}, Categoria: {chamado['categoria']}, Prioridade: {chamado['prioridade']}, Status: {chamado['status']}")

def buscar_chamados(chamados):
    while True:
        try:
            id_chamado = int(input("Digite o ID do chamado que deseja buscar: "))
            
            for chamado in chamados:
                if chamado['id'] == id_chamado:
                    return chamado
                            
            print("Chamado não encontrado!")
        except ValueError:
            print('Digite apenas números!')

def atualizar_status(chamados):
    while True:
        try:
            id_chamado = int(input("Digite o ID do chamado que deseja buscar: "))
            
            for chamado in chamados:
                if chamado['id'] == id_chamado:
                    novo_status = input("Digite o novo status do chamado (Aberto, Em andamento, Concluído): ").strip().lower()
                    
                    while novo_status not in ['aberto', 'em andamento', 'concluído']:
                        print("Status inválido!")
                        novo_status = input("Digite o novo status do chamado novamente: ").strip().lower()
                    
                    chamado['status'] = novo_status
                    return chamado
            
            print("Chamado não encontrado!")
        except ValueError:
            print('Digite apenas números!')
        
def alterar_prioridade(chamados):
    while True:
        try:
            id_chamado = int(input("Digite o ID do chamado que deseja buscar: "))
            
            for chamado in chamados:
                if chamado['id'] == id_chamado:
                    nova_prioridade = input("Digite a nova prioridade do chamado (Alta, Média, Baixa): ").strip().lower()
                    
                    while nova_prioridade not in ['alta', 'média', 'baixa']:
                        print("Prioridade inválida!")
                        nova_prioridade = input("Digite a nova prioridade do chamado novamente: ").strip().lower()
                    
                    chamado['prioridade'] = nova_prioridade
                    return chamado
                
            print("Chamado não encontrado!")
        except ValueError:
            print('Digite apenas números!')

def remover_chamado(chamados):
    while True:
        try:
            id_chamado = int(input("Digite o ID do chamado que deseja remover: "))
            
            for chamado in chamados:
                if chamado['id'] == id_chamado:
                    chamados.remove(chamado)
                    print("Chamado removido com sucesso!")
                    return chamados
                
            print("Chamado não encontrado!")
        except ValueError:
            print('Digite apenas números!')

def filtrar_por_status(chamados):
    while True:
        filtro_status = input("Digite o status que deseja filtrar (Aberto, Em andamento, Concluído): ").strip().lower()
        
        if filtro_status not in ['aberto', 'em andamento', 'concluído']:
                    print("Status inválido!")
        else:
            for chamado in chamados:
                if chamado['status'] == filtro_status:
                    print(f"ID: {chamado['id']}, Nome: {chamado['nome']}, Descrição: {chamado['descricao']}, Categoria: {chamado['categoria']}, Prioridade: {chamado['prioridade']}, Status: {chamado['status']}")
                
            break
                      
chamados = []
main()