# 🤖 React Agent Google Calendar

> Assistente pessoal inteligente com integração ao Google Calendar usando LangGraph e ReAct Pattern

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)](https://www.langchain.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Latest-orange.svg)](https://langchain-ai.github.io/langgraph/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Sobre o Projeto

Um assistente conversacional inteligente que utiliza o padrão **ReAct** (Reasoning + Acting) para interagir com o Google Calendar e executar tarefas do dia a dia. O agente é capaz de raciocinar sobre as solicitações do usuário e decidir autonomamente quais ferramentas utilizar para fornecer respostas precisas.

### ✨ Características Principais

- 🧠 **Agente ReAct** - Raciocínio e ação integrados para tomada de decisões
- 📅 **Integração Google Calendar** - Gerenciamento completo da agenda
- 💬 **Interface Conversacional** - Interação natural em português brasileiro
- 🔧 **Ferramentas Modulares** - Arquitetura extensível com múltiplas tools
- 🎨 **UI Rica** - Interface de terminal colorida com Rich

## 🛠️ Tecnologias Utilizadas

### Core Framework
- **[LangChain](https://www.langchain.com/)** - Framework para desenvolvimento de aplicações com LLMs
- **[LangGraph](https://langchain-ai.github.io/langgraph/)** - Orquestração de agentes com grafos de estado
- **[Python 3.12+](https://www.python.org/)** - Linguagem de programação

### LLM & Providers
- **[Ollama](https://ollama.ai/)** - Execução local de modelos (Qwen 2.5:7b)
- **[Google Generative AI](https://ai.google.dev/)** - Suporte alternativo para modelos Google

### APIs & Integrações
- **[Google Calendar API](https://developers.google.com/calendar)** - Gerenciamento de eventos
- **[google-auth-oauthlib](https://github.com/googleapis/google-auth-library-python-oauthlib)** - Autenticação OAuth 2.0
- **[google-api-python-client](https://github.com/googleapis/google-api-python-client)** - Cliente oficial Google

### Persistência & Estado
- **[LangGraph Checkpointer](https://langchain-ai.github.io/langgraph/reference/checkpoints/)** - Gerenciamento de estado

### Interface & UX
- **[Rich](https://rich.readthedocs.io/)** - Terminal UI com formatação Markdown
- **[Pydantic](https://docs.pydantic.dev/)** - Validação de dados e tipos

## 🎯 Ferramentas (Tools) Disponíveis

### 1. 📅 **Google Calendar**

#### `list_calendar_events`
Lista os próximos eventos da agenda do usuário
```python
Args:
  - max_results (int): Número máximo de eventos (padrão: 10)
Returns:
  - String formatada com eventos ou mensagem se vazio
```

#### `create_calendar_event`
Cria novos eventos no calendário
```python
Args:
  - summary (str): Título do evento
  - start_time (str): Data/hora início (ISO: YYYY-MM-DDTHH:MM:SS)
  - end_time (str): Data/hora término (ISO: YYYY-MM-DDTHH:MM:SS)
  - description (Optional[str]): Descrição do evento
  - location (Optional[str]): Local do evento
Returns:
  - Link do evento criado ou mensagem de erro
```

**Regras de Negócio:**
- ⏰ Horário comercial: 08:00 - 18:00
- 📆 Dias úteis: Segunda a sexta-feira
- ⏱️ Duração padrão: 1 hora
- 🚫 Não permite eventos sobrepostos

### 2. 🧮 **Calculadora**

Operações matemáticas básicas:
- `multiply` - Multiplicação
- `add` - Adição
- `subtract` - Subtração
- `divide` - Divisão

### 3. 🆔 **Validador de CPF**

#### `validar_cpf`
Valida números de CPF segundo regras brasileiras
```python
Args:
  - cpf (str): CPF para validação
Returns:
  - bool: True se válido, False caso contrário
```

## 🚀 Como Executar

### Pré-requisitos

1. **Python 3.12+** instalado
2. **Ollama** instalado e rodando (ou conta Google AI)
3. **Credenciais Google Calendar API**

### Configuração

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/react-agent-googlecalendar.git
cd react-agent-googlecalendar
```

2. **Crie um ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Configure Google Calendar API**

   a) Acesse [Google Cloud Console](https://console.cloud.google.com/)
   
   b) Crie um projeto e habilite a **Google Calendar API**
   
   c) Crie credenciais OAuth 2.0 (tipo: Desktop App)
   
   d) Baixe o arquivo JSON e salve como:
   ```
   src/tools/credentials.json
   ```

5. **Configure o modelo LLM** (Ollama)
```bash
# Instale o modelo
ollama pull qwen2.5:7b

# Inicie o servidor Ollama
ollama serve
```

6. **Execute o projeto**
```bash
python main.py
```

Na primeira execução, será aberta uma janela do navegador para autenticação Google. Um arquivo `token.json` será criado para reutilização.

## 📂 Estrutura do Projeto

```
react-agent-googlecalendar/
├── main.py                      # Ponto de entrada da aplicação
├── requirements.txt             # Dependências do projeto
├── README.md                    # Documentação
├── .env                         # Variáveis de ambiente (não versionado)
├── token.json                   # Token Google (gerado automaticamente)
│
└── src/
    ├── __init__.py
    ├── graph.py                 # Definição do grafo ReAct (LangGraph)
    ├── state.py                 # Definição do estado do agente
    │
    ├── prompts/
    │   ├── __init__.py
    │   └── prompts.py           # System prompt do agente
    │
    ├── tools/
    │   ├── __init__.py
    │   ├── tools.py             # Registro de todas as tools
    │   ├── google_calendar.py   # Tools do Google Calendar
    │   ├── calculator.py        # Ferramentas de cálculo
    │   ├── valida_cpf.py        # Validador de CPF
    │   └── credentials.json     # Credenciais Google (não versionado)
    │
    └── utils/
        ├── __init__.py
        └── utils.py             # Utilitários (carregamento LLM, etc)
```

## 💡 Exemplos de Uso

### Consultar Agenda
```
Você: Quais são meus compromissos de amanhã?
```

### Criar Evento
```
Você: Marque uma reunião com a equipe dia 10 às 14h
```

### Validar CPF
```
Você: Valide o CPF 123.456.789-09
```

### Cálculos
```
Você: Quanto é 47 vezes 23?
```

## 🧪 Padrão ReAct

O agente utiliza o padrão **ReAct** (Reasoning + Acting), que alterna entre:

1. **💭 Thought** - Raciocínio sobre o que fazer
2. **🔧 Action** - Execução de uma ferramenta
3. **📊 Observation** - Análise do resultado
4. **✅ Answer** - Resposta final ao usuário

Exemplo de fluxo:
```
Usuário: "Marque reunião dia 7 às 14h"
  ↓
Thought: "Preciso verificar se há conflito na agenda"
  ↓
Action: list_calendar_events()
  ↓
Observation: "Agenda livre às 14h"
  ↓
Action: create_calendar_event(...)
  ↓
Answer: "✅ Evento criado com sucesso!"
```

## 🔒 Segurança

- 🔐 **OAuth 2.0** - Autenticação segura com Google
- 🚫 **Tokens não versionados** - `token.json` e `credentials.json` no `.gitignore`
- 🔒 **Escopos limitados** - Apenas acesso ao Calendar API

## 📝 Variáveis de Ambiente

Crie um arquivo `.env` na raiz (opcional):

```env
# LLM Provider (ollama ou google)
LLM_PROVIDER=ollama

# Ollama Configuration
OLLAMA_MODEL=qwen2.5:7b
OLLAMA_BASE_URL=http://localhost:11434

# Google AI (opcional)
GOOGLE_API_KEY=your_api_key_here
```

