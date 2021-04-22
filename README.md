## Conceitos de mineração e blockchain
Esse repositorio é uma aplicação simples dos conceitos de blockchain e mineração dos blocos

### Tecnologias utilizadas
* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [sqlite](https://www.sqlite.org/index.html)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Marshmallow](https://marshmallow.readthedocs.io/en/stable/)

### Iniciando backend localmente

1. Após clonar repositório
2. Criar virtual enviroment na raiz do projeto (repositório) utilizando: ```python3 -m venv venv```
3. Ativando ambiente virtual no MAC/Linux utilize: ```source ./venv/bin/activate```
4. Assim que ambiente for ativado, instale as dependências: ```pip install -r requirements.txt```
5. Crie um banco como o nome que desejar, usando o comando ```sqlite3 ./app/main/database/'nome_do_banco.db'```
6. Após criar banco, execute essa sequência de comandos para realizar a migrations:
```
  1. python manage.py db init
  2. python manage.py db migrate
  3. python manage.py db upgrade
```
7. Após realizar as migrations, renomeie o arquivo **.env.example** para __.env__ e configure conforme necessário.
8. Por último, após ajustar sua **.env** execute o comando para iniciar a aplicação: ```python manage.py run```

### Estrutura do projeto

| Nome do arquivo 　　　　　　　　　　　　　　| Descrição 　　　　　　　　<br><br>|
| :--  | :--         |
| `├── app ` (_diretorio_) | _Contém todo código da aplicação_ |
| `│ 　├── init.py` | Instânciamenteo da API |
| `│　 └── main` (_diretorio_) | Diretório que mantém atoda parte lógica da API |
| `│　　　├── controller` (_diretorio_) | Diretório que contém endpoints da API Rest |
| `│　　　├── database` (_diretorio_) | Diretório que contém o arquivo com o banco de dados |
| `│　　　├── model` (_diretorio_) | Diretório que contém os modelos do banco de dados |
| `│　　　├── service` (_diretorio_) | Diretório que mantém toda regra de negocio dentro da API |
| `│　　　└── util` (_diretorio_) | Diretório contém utilidades que irão ajudar na execução da API |
| `└── venv ` (_diretorio_)  | _Todas dependencias da API ficam nesse diretorio_ |
| `└── .env ` | _Variáveis de ambientes da API_ |
| `└── requirements.txt ` | _Todas dependencias necessárias para rodar aplicação ficam nesse arquivo_ |
| `└── manage.py ` | _CLI da aplicação, todos comandos ficam ali e serve para iniciar aplicação_ |