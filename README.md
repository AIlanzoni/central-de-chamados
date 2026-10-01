# 🎫 Sistema de Chamados (Helpdesk) em Python

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-em%20constru%C3%A7%C3%A3o-yellow)
![Interface](https://img.shields.io/badge/interface-CLI-lightgrey)

Aplicação de linha de comando para **abertura, consulta e acompanhamento de chamados de suporte de TI**, inspirada no fluxo real de um service desk. O projeto está em evolução contínua e serve como laboratório para praticar lógica de programação, modelagem de dados e boas práticas de código.

> 🚧 **Projeto em construção** — novas funcionalidades estão sendo adicionadas aos poucos (veja o [Roadmap](#roadmap)).

---

## 📌 Funcionalidades atuais

- ✅ Abertura de chamados com solicitante, descrição, categoria e prioridade
- ✅ Validação de categoria e prioridade, com nova solicitação até o dado ser válido
- ✅ Geração automática de ID sequencial
- ✅ Status inicial automático (`Aberto`)
- ✅ Listagem de todos os chamados registrados
- ✅ Busca de chamado por ID
- ✅ Atualização de status (`Aberto`, `Em andamento`, `Concluído`)
- ✅ Alteração de prioridade de um chamado existente

### Categorias aceitas
`Hardware` · `Software` · `Rede` · `Acesso` · `Suporte`

### Prioridades aceitas
`Alta` · `Média` · `Baixa`

### Status disponíveis
`Aberto` → `Em andamento` → `Concluído`

---

## 🧱 Estrutura do chamado

Cada chamado é representado por um dicionário:

```python
{
    "id": 1,
    "nome": "Maria Silva",
    "descricao": "Computador não liga",
    "categoria": "Hardware",
    "prioridade": "Alta",
    "status": "Aberto"
}
```

---

## ⚙️ Principais funções

| Função | O que faz |
|---|---|
| `criar_chamado(id_chamado)` | Coleta e valida os dados e monta o chamado |
| `adicionar_chamado(chamados)` | Gera o ID e adiciona o chamado à lista |
| `listar_chamados(chamados)` | Exibe todos os chamados registrados |
| `buscar_chamados(chamados)` | Localiza um chamado pelo ID |
| `atualizar_status(chamados)` | Altera o status de um chamado |
| `alterar_prioridade(chamados)` | Altera a prioridade de um chamado |

---

## ▶️ Como executar

**Pré-requisito:** Python 3.10 ou superior.

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
Digite o nome do solicitante: Maria Silva
Digite a descrição do chamado: Computador não liga
Digite a categoria do chamado: Hardware
Digite a prioridade do chamado (Alta, Média, Baixa): Alta
...
Digite o ID do chamado que deseja buscar: 1
Digite o novo status do chamado (Aberto, Em andamento, Concluído): Em andamento
```

---

<a id="roadmap"></a>

## 🗺️ Roadmap

### ✅ v0.1 — Base (concluído)
- [x] Abertura de chamados com validação de categoria e prioridade
- [x] ID sequencial e status inicial automático
- [x] Listagem de chamados

### 🚧 v0.2 — Usabilidade (em andamento)
- [x] Busca de chamado por ID
- [x] Atualização de status (`Aberto` → `Em andamento` → `Concluído`)
- [x] Alteração de prioridade
- [ ] Menu interativo (abrir, listar, buscar, atualizar, encerrar)
- [ ] Registro de data/hora de abertura e fechamento

### 🔜 v0.3 — Organização do código
- [ ] Refatoração para orientação a objetos (classe `Chamado`)
- [ ] Separação em módulos (modelo, serviço, interface)

### 🔜 v0.4 — Persistência
- [ ] Salvar e carregar chamados em JSON
- [ ] Migrar para banco de dados SQL (SQLite)

### 🔜 v0.5 — Qualidade
- [ ] Tratamento de entradas inválidas (ex.: ID não numérico)
- [ ] Testes automatizados com `pytest`

### 🔜 v0.6 — Consultas e métricas
- [ ] Filtros por categoria, prioridade e status
- [ ] Relatórios (chamados por categoria, tempo médio de resolução)

### 💡 Futuro
- [ ] API REST (FastAPI) e/ou interface web

---

## 🛠️ Tecnologias

- **Python 3**
- Estruturas de dados nativas (listas e dicionários)
- Funções, laços de repetição e validação de entrada

---

## 🎯 Objetivos de aprendizado

- Modelagem de um problema real de suporte de TI em código
- Validação e tratamento de dados de entrada
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
