# Documentação da API - Sistema de Apoio à Decisão

## Vinicius Marques Santos Silva - 0070356

## Introdução

Esta API foi desenvolvida para um Sistema de Apoio à Decisão, focado em gerenciar informações de produtos, clientes e vendas. Ela segue os princípios SOLID para garantir uma arquitetura de software bem estruturada, fácil de manter e escalável.

Os princípios SOLID foram aplicados de forma a garantir que o código seja modular, extensível e de fácil manutenção.

---

## Princípios SOLID Aplicados

### 1. **Single Responsibility Principle (SRP) - Princípio da Responsabilidade Única**

O SRP afirma que uma classe deve ter uma única razão para mudar. Ou seja, cada classe e módulo deve ser responsável por uma única parte da funcionalidade do sistema.

**Aplicação na API:**
- **ProdutoController**: Responsável por operações relacionadas a produtos, como listagem, produtos mais vendidos e produtos com baixo estoque.
- **VendaController**: Responsável por operações relacionadas a vendas, como listagem e manipulação de dados de vendas.
- **ClienteController**: Responsável por todas as operações relacionadas a clientes, como listagem e análise de clientes com mais compras.

Cada controlador tem uma responsabilidade bem definida, o que facilita a manutenção e a clareza do código.

---

### 2. **Open/Closed Principle (OCP) - Princípio Aberto/Fechado**

Este princípio afirma que uma classe deve ser aberta para extensão, mas fechada para modificação. Ou seja, podemos adicionar novas funcionalidades sem modificar o código existente.

**Aplicação na API:**
- A API foi projetada de forma modular, com controladores e modelos separados para **Produto**, **Venda** e **Cliente**. Caso seja necessário adicionar novas funcionalidades, como novos filtros ou novos tipos de relatórios, podemos estender os controladores e modelos existentes sem alterar os arquivos originais.
- A adição de novos endpoints, como por exemplo, uma rota para filtrar vendas por data ou valor, pode ser feita de maneira simples, sem modificar o funcionamento dos endpoints já existentes.

---

### 3. **Liskov Substitution Principle (LSP) - Princípio da Substituição de Liskov**

O LSP afirma que uma classe derivada deve ser substituível por sua classe base sem alterar o comportamento do programa.

**Aplicação na API:**
- Embora o código não utilize herança de classes diretamente, o LSP é aplicado indiretamente por meio da estrutura modular da API. Caso seja necessário introduzir novos tipos de **Produto** ou **Cliente**, isso pode ser feito sem modificar as funcionalidades existentes da API.
- As classes base podem ser substituídas por novas implementações sem impactar os controladores ou a lógica de negócio, permitindo a expansão do sistema de forma segura e sem quebras.

---

### 4. **Interface Segregation Principle (ISP) - Princípio da Segregação da Interface**

O ISP recomenda que as interfaces não devem forçar os clientes a depender de métodos que não utilizam. Ou seja, devemos criar interfaces pequenas e especializadas, em vez de interfaces grandes e genéricas.

**Aplicação na API:**
- Cada controlador tem métodos específicos para sua funcionalidade, por exemplo:
  - **ProdutoController** tem métodos como `listar_produtos()`, `produtos_mais_vendidos()` e `produtos_baixo_estoque()`.
  - **VendaController** tem métodos voltados para operações de vendas.
  - **ClienteController** tem métodos específicos para operações com clientes.
  
Isso evita dependências desnecessárias entre os controladores e garante que as interfaces de cada controlador sejam pequenas, claras e coesas.

---

### 5. **Dependency Inversion Principle (DIP) - Princípio da Inversão de Dependência**

O DIP afirma que as classes de alto nível não devem depender de classes de baixo nível, mas ambas devem depender de abstrações. Além disso, as abstrações não devem depender de detalhes; os detalhes devem depender das abstrações.

**Aplicação na API:**
- Embora a API não tenha uma injeção de dependências explícita, ela segue o DIP ao garantir que os controladores não dependam diretamente de detalhes de implementação, como o banco de dados.
- O acesso ao banco de dados e outras operações de persistência são abstraídos através de camadas intermediárias, como os **serviços de repositório**, o que permite que o código de controle permaneça desacoplado da implementação concreta da persistência de dados.
- Isso permite que mudanças na implementação de banco de dados (de SQL para NoSQL, por exemplo) não impactem os controladores e a lógica de negócios da aplicação.

---

## Estrutura do Projeto

A estrutura do projeto é organizada de forma modular para facilitar a manutenção e a escalabilidade. Abaixo está o mapeamento dos principais arquivos e diretórios:

```
├── main.py                # Arquivo principal que inicializa a API
├── requirements.txt       # Arquivo contendo a listagem de dependencias do projeto 
├── connector/
│   └── database.py       # Classe controladora da conexão com o Banco de Dados
├── utils/
│   └── basemodel.py       # Modelo base para entidades compartilhadas
├── Cliente/
│   ├── cliente_controller.py # Controlador das operações com clientes
│   ├── cliente_model.py    # Modelos dos dados de clientes
│   └── cliente_view.py     # Visões para representação dos dados de clientes
├── Produto/
│   ├── produto_controller.py # Controlador das operações com produtos
│   ├── produto_model.py     # Modelos dos dados de produtos
│   └── produto_view.py      # Visões para representação dos dados de produtos
├── Venda/
│   ├── venda_controller.py  # Controlador das operações com vendas
│   ├── venda_model.py       # Modelos dos dados de vendas
│   └── venda_view.py        # Visões para representação dos dados de vendas
└── static/
    └── index.html  
```

### Arquivos Importantes

- **`produto_controller.py`**, **`venda_controller.py`** e **`cliente_controller.py`**: Controladores responsáveis pelas rotas da API e pela lógica de processamento de dados.
- **`produto.py`**, **`venda.py`** e **`cliente.py`**: Modelos que representam as entidades de Produto, Venda e Cliente.
- **`produto_repository.py`**, **`venda_repository.py`** e **`cliente_repository.py`**: Camada de persistência responsável por acessar e manipular os dados no banco de dados.
- **`produto_service.py`**, **`venda_service.py`** e **`cliente_service.py`**: Serviços que abstraem a lógica de negócios e permitem fácil extensão sem modificar os controladores.
- **`main.py`**: Arquivo principal para inicialização da aplicação.

---

## Como Rodar o Projeto

### 1. Clonando o Repositório

Clone o repositório do projeto para sua máquina local.

```bash
git clone <URL_DO_REPOSITORIO>
cd <DIRETORIO_DO_REPOSITORIO>
```

### 2. Instalando as Dependências

Instale as dependências do projeto usando o `pip`:

```bash
pip install -r requirements.txt
```

O arquivo `requirements.txt` contém todas as bibliotecas necessárias para rodar a API, incluindo o **FastAPI** e o **uvicorn** para execução do servidor.

### 3. Rodando o Servidor

Para iniciar a aplicação, execute o seguinte comando:

```bash
uvicorn app.main:app --reload
```

O servidor estará disponível em `http://localhost:8000`.

### 4. Acessando a Documentação Interativa

A API possui documentação interativa via **Swagger**. Após iniciar o servidor, você pode acessar a documentação em:

```
http://localhost:8000/docs
```

---

## Conclusão

A API foi projetada e desenvolvida com base nos princípios SOLID, visando a criação de um sistema modular, flexível e fácil de manter. Cada componente do sistema (Produto, Venda, Cliente) foi cuidadosamente isolado e estruturado para facilitar futuras extensões sem impactar o funcionamento das funcionalidades existentes.

A aplicação desses princípios garante que o código seja de fácil manutenção e escalabilidade à medida que novos requisitos sejam introduzidos.

