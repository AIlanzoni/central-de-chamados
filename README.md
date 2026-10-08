# 🎫 Central de Chamados (Helpdesk) em Python

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-em%20constru%C3%A7%C3%A3o-yellow)
![Interface](https://img.shields.io/badge/interface-CLI-lightgrey)

Aplicação de linha de comando para **abertura, consulta, filtragem e acompanhamento de chamados de suporte de TI**, inspirada no fluxo real de um service desk. O projeto está em evolução contínua e serve como laboratório para praticar lógica de programação, modelagem de dados e boas práticas de código.

> 🚧 **Projeto em construção** — novas funcionalidades estão sendo adicionadas aos poucos (veja o [Roadmap](#roadmap)).

---

## 📌 Funcionalidades atuais

**Gestão de chamados**
- ✅ Menu interativo com navegação por opções numeradas
- ✅ Abertura de chamados com solicitante, descrição, categoria e prioridade
- ✅ Geração de **ID único** (sorteio com verificação de duplicidade)
- ✅ Listagem e busca de chamado por ID
- ✅ Atualização de status (`aberto`, `em andamento`, `concluído`)
- ✅ Alteração de prioridade
- ✅ Remoção de chamados

**Consultas e métricas**
- ✅ Filtro de chamados por status
- ✅ Filtro de chamados por prioridade
- ✅ Contagem de chamados por status
- ✅ Contagem de chamados por prioridade

**Persistência**
- ✅ Salvamento dos chamados em arquivo `chamados.json`
- ✅ Carregamento automático dos dados ao iniciar o programa
- ✅ Opção de recarregar os dados do arquivo pelo menu

**Qualidade das entradas**
- ✅ Validação de categoria, prioridade e status, solicitando o dado novamente até ficar correto
- ✅ Tratamento de entradas inválidas (ex.: texto no lugar de número) com `try/except`
- ✅ Normalização das entradas (ignora espaços extras e diferenças entre maiúsculas e minúsculas)

### Menu

```text
===== CENTRAL DE CHAMADOS =====
1. Adicionar chamado
2. Listar chamados
3. Buscar chamado
4. Atualizar status do chamado
5. Alterar prioridade do chamado
6. Remover chamado
7. Filtrar status dos chamados
8. Filtrar prioridade dos chamados
9. Contar status dos chamados
10. Contar prioridade dos chamados
11. Salvar chamados em arquivo JSON
12. Carregar chamados de arquivo JSON
0. Sair
```

### Valores aceitos

| Campo | Valores |
|---|---|
| Categoria | `hardware` · `software` · `rede` · `acesso` · `suporte` |
| Prioridade | `alta` · `média` · `baixa` |
| Status | `aberto` → `em andamento` → `concluído` |

---

## 🧱 Estrutura do chamado

Cada chamado é representado por um dicionário e armazenado em `chamados.json`:

```json
{
    "id": 482,
    "nome": "maria silva",
    "descricao": "computador não liga",
    "categoria": "hardware",
    "prioridade": "alta",
    "status": "aberto"
}
```

---

## ⚙️ Principais funções

| Função | O que faz |
|---|---|
| `main()` | Exibe o menu e direciona para cada operação |
| `criar_chamado(id_chamado)` | Coleta e valida os dados e monta o chamado |
| `adicionar_chamado(chamados)` | Gera um ID único e adiciona o chamado à lista |
| `listar_chamados(chamados)` | Exibe todos os chamados registrados |
| `buscar_chamados(chamados)` | Localiza um chamado pelo ID |
| `atualizar_status(chamados)` | Altera o status de um chamado |
| `alterar_prioridade(chamados)` | Altera a prioridade de um chamado |
| `remover_chamado(chamados)` | Remove um chamado pelo ID |
| `filtrar_por_status(chamados)` | Lista os chamados de um determinado status |
| `filtrar_por_prioridade(chamados)` | Lista os chamados de uma determinada prioridade |
| `contar_chamados_status(chamados)` | Exibe o total de chamados por status |
| `contar_chamados_prioridade(chamados)` | Exibe o total de chamados por prioridade |
| `salvar_chamados(chamados)` | Grava os chamados em `chamados.json` |
| `carregar_chamados()` | Lê os chamados de `chamados.json` |

---

## ▶️ Como executar

**Pré-requisito:** Python 3.10 ou superior (usa apenas a biblioteca padrão, sem dependências externas).

```bash
# 1. Clone o repositório
git clone https://github.com/AIlanzoni/central-de-chamados.git

# 2. Entre na pasta
cd central-de-chamados

# 3. Execute
python main.py
```

### Exemplo de uso

```text
Escolha uma opção: 1
Digite o nome do solicitante: Maria Silva
Digite a descrição do chamado: Computador não liga
Digite a categoria do chamado: Hardware
Digite a prioridade do chamado (Alta, Média, Baixa): Alta

Escolha uma opção: 9
Total de chamados abertos: 1
Total de chamados em andamento: 0
Total de chamados concluídos: 0

Escolha uma opção: 11
```

> 💡 Os chamados são carregados automaticamente ao abrir o programa. Para não perder alterações, use a **opção 11** antes de sair.

---

<a id="roadmap"></a>

## 🗺️ Roadmap

### ✅ v0.1 — Base (concluído)
- [x] Abertura de chamados com validação de categoria e prioridade
- [x] ID e status inicial automáticos
- [x] Listagem de chamados

### 🚧 v0.2 — Usabilidade (em andamento)
- [x] Menu interativo
- [x] Busca por ID, atualização de status e alteração de prioridade
- [x] Remoção de chamados
- [x] Tratamento de entradas inválidas
- [x] IDs únicos mesmo após remoções
- [ ] Opção de cancelar uma operação ao informar um ID inexistente
- [ ] Registro de data/hora de abertura e fechamento

### 🚧 v0.3 — Consultas e métricas (em andamento)
- [x] Filtros por status e prioridade
- [x] Contagem de chamados por status e prioridade
- [ ] Filtro por categoria
- [ ] Relatórios avançados (chamados por categoria, tempo médio de resolução)

### 🚧 v0.4 — Persistência (em andamento)
- [x] Salvar e carregar chamados em JSON
- [ ] Salvamento automático a cada alteração
- [ ] Tratamento de arquivo JSON corrompido
- [ ] Migrar para banco de dados SQL (SQLite)

### 🔜 v0.5 — Organização do código
- [ ] Refatoração para orientação a objetos (classe `Chamado`)
- [ ] Separação em módulos (modelo, serviço, interface)
- [ ] Formatação amigável na exibição dos chamados

### 🔜 v0.6 — Qualidade
- [ ] Testes automatizados com `pytest`

### 💡 Futuro
- [ ] API REST (FastAPI) e/ou interface web

---

## 🛠️ Tecnologias

- **Python 3** (biblioteca padrão: `json`, `random`)
- Estruturas de dados nativas (listas e dicionários)
- Funções, laços de repetição e tratamento de exceções (`try/except`)
- Persistência em arquivo JSON

---

## 🎯 Objetivos de aprendizado

- Modelagem de um problema real de suporte de TI em código
- Validação e tratamento de dados de entrada
- Persistência de dados e geração de métricas simples
- Organização do código em funções com responsabilidades claras
- Evolução incremental de um projeto (versionamento com Git)

---

## 👤 Autor

**Arthur Lanzoni**
Analista de Sistemas | Formado em Análise e Desenvolvimento de Sistemas

- 💼 LinkedIn: [Arthur Lanzoni](https://www.linkedin.com/in/arthurlanzoni)
- 🐙 GitHub: [AIlanzoni](https://github.com/AIlanzoni)
- ✉️ E-mail: arthurlanzoni08@gmail.com

---

⭐ Se o projeto te interessou, deixe uma estrela e acompanhe as próximas atualizações!
