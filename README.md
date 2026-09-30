# 🎫 Sistema de Chamados (Helpdesk) em Python

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-em%20constru%C3%A7%C3%A3o-yellow)
![Interface](https://img.shields.io/badge/interface-CLI-lightgrey)

Aplicação de linha de comando para **abertura, registro e listagem de chamados de suporte de TI**, inspirada no fluxo real de um service desk. O projeto está em evolução contínua e serve como laboratório para praticar lógica de programação, modelagem de dados e boas práticas de código.

> 🚧 **Projeto em construção** — novas funcionalidades estão sendo adicionadas aos poucos.
> 
---

## 📌 Funcionalidades atuais

- ✅ Abertura de chamados com solicitante, descrição, categoria e prioridade
- ✅ Validação de dados de entrada (categoria e prioridade) com valores padrão seguros
- ✅ Geração automática de ID sequencial
- ✅ Status inicial automático (`Aberto`)
- ✅ Listagem de todos os chamados registrados

### Categorias aceitas
`Hardware` · `Software` · `Rede` · `Acesso` · `Suporte`

### Prioridades aceitas
`Alta` · `Média` · `Baixa`

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
ID: 1, Nome: Maria Silva, Descrição: Computador não liga, Categoria: Hardware, Prioridade: Alta, Status: Aberto
```

---

## 🗺️ Roadmap

### ✅ v0.1 — Base (concluído)
- [x] Abertura de chamados com validação de categoria e prioridade
- [x] ID sequencial e status inicial automático
- [x] Listagem de chamados

### 🚧 v0.2 — Usabilidade (em andamento)
- [ ] Menu interativo (abrir, listar, buscar, atualizar, encerrar)
- [ ] Atualização de status (`Aberto` → `Em andamento` → `Resolvido`)
- [ ] Registro de data/hora de abertura e fechamento

### 🔜 v0.3 — Organização do código
- [ ] Refatoração para orientação a objetos (classe `Chamado`)
- [ ] Separação em módulos (modelo, serviço, interface)

### 🔜 v0.4 — Persistência
- [ ] Salvar e carregar chamados em JSON
- [ ] Migrar para banco de dados SQL (SQLite)

### 🔜 v0.5 — Qualidade
- [ ] Testes automatizados com `pytest`

### 🔜 v0.6 — Consultas e métricas
- [ ] Busca e filtros por categoria, prioridade e status
- [ ] Relatórios (chamados por categoria, tempo médio de resolução)

### 💡 Futuro
- [ ] API REST (FastAPI) e/ou interface web

---

## 🛠️ Tecnologias

- **Python 3**
- Estruturas de dados nativas (listas e dicionários)
- Funções e validação de entrada

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
