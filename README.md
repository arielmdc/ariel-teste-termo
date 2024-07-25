
# Termo Game

Este é um projeto simples para simular o jogo "Termo" e realizar testes unitários utilizando pytest.

## Estrutura do Projeto

- `termo_game.py`: Contém a classe `TermoGame`, que implementa a lógica do jogo.
- `tests/`: Contém os testes unitários para a classe `TermoGame`.
  - `test_termo_game.py`: Contém os testes para verificar a funcionalidade do jogo.
- `requirements.txt`: Lista de dependências do projeto (opcional).
- `README.md`: Descrição do projeto.

## Como Executar o Projeto

### 1. Clonar o Repositório

Clone o repositório para sua máquina local usando o comando:

```bash
git clone <URL_DO_REPOSITORIO>
```

### 2. Criar um Ambiente Virtual (opcional)

Para evitar conflitos com outras dependências do Python na sua máquina, é recomendado criar um ambiente virtual. Execute os seguintes comandos:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instalar Dependências

Instale as dependências do projeto listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Executar os Testes

Para executar os testes e verificar se o código está funcionando corretamente, utilize o pytest:

```bash
pytest -vv
```