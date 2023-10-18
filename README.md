# maisTODOSTest
Python test to maisTODOS


## Stack utilizada

**Back-end:** Python, Flask

**Database** Postgres

**Docker** Dockerfile, docker-compose

## Requisitos

- Python (versão 3.8)
- pip
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-RESTful
- Flask-JWT-Extended
- Outras dependências (verifique o arquivo `requirements.txt`)
- Certifique-se de ter o Docker e o Docker Compose instalados na sua máquina. Você pode baixá-los em [Docker](https://www.docker.com/get-started). (Opcional)

## Instalação

1. Clone este repositório para o seu ambiente de desenvolvimento.

```shell
git clone https://github.com/Luansantosdevpy/maisTODOSTest.git
```

2. Navegue até o diretório do projeto.
```shell
cd maisTODOSTest
```

3. Crie um ambiente virtual (recomendado).
```shell
python -m venv venv
```

4. Ative o ambiente virtual.

  - No Windows:
```shell
venv\Scripts\activate
```


  - No macOS e Linux:
```shell
source venv/bin/activate
```

5. Instale as dependências do projeto.
```shell
pip install -r requirements.txt
```

6. Copie o env.sample para o env
```shell
  cp env.sample .env
```

7. Modifique as variáveis do seu .env

8. Execute as migrações do banco de dados.
```shell
flask db init
flask db migrate
flask db upgrade
```

9. Inicie o aplicativo.
```shell
flask run
```

## Via Docker

1. Crie um arquivo .env na raiz do projeto para configurar as variáveis de ambiente necessárias, como no env.sample.
```shell
cp .env.sample .env
```

2. Modifique as variáveis do seu .env

3. Inicie os contêineres:
```shell
docker-compose up
```
Isso iniciará o aplicativo Flask e o banco de dados PostgreSQL em contêineres separados.

4. Acesse o aplicativo em seu cliente REST em http://localhost:5000. (Collection do Insomnia [aqui](/collection/todos.json))
Para utilizar a collection, basta fazer o download do arquivo e importar no Insomnia. Lembrar de trocar as envs url e token sempre pelos valores corretos da sua aplicação.

Divirta-se.

## Uso
Registre-se ou faça login para começar a usar o sistema.
É necessário usar o token fornecido no login, para poder criar um cartão de crédito.
Crie, edite, exclua e visualize cartões de crédito.



## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env
Esteja a vontade para criar os valores de acordo com o que preferir

`DB_POSTGRES_USER`

`DB_POSTGRES_PASSWORD`

`DB_POSTGRES_HOST`

`DB_POSTGRES_PORT`

`DB_POSTGRES_NAME`

`DATABASE_URL=postgresql://user:password@host/name`
## Documentação
!Importante Deve estar com a aplicação rodando para funcionar

[Documentação Swagger](http://localhost:5000/api/docs)


## Demonstração
Para ver a demonstração da documentação, basta acessar o link abaixo:

[Demonstração da documentação](https://www.youtube.com/watch?v=4U_yC0YXfks)


## Rodando os testes

Para rodar os testes, rode o seguinte comando. Ele exibirá o retorno de testes unitários e de integração.

```bash
  coverage run -m pytest
```
Para visualizar o resultado dos testes:

```bash
  coverage report
```

## Possíveis erros
É possível encontrar um erro ao rodar a aplicação com docker. Não consegui descobrir a tempo o que está causando o erro. Caso aconteça, tente fazer o seguinte:
rode o seguinte comando do docker
```shell
  docker-compose up --scale app=0 --scale postgres=1
```
Faça isso para rodar apenas o banco
Rode localmente tudo como foi ensinado anteriormente, já com o banco montado pelo docker-compose para rodar a aplicação localmente.

É possível encontrar um erro no psycopg2 ao instalar o requirements.txt localmente, esse erro: Error: pg_config executable not found.
Caso se depare com esse erro, faça o seguinte:
```shell
  sudo apt-get install libpq-dev
```

Caso encontre erros para gerar as migrations, segue as queries para criar as tabelas:
```shell
CREATE TABLE credit_cards (
    id SERIAL PRIMARY KEY,
    exp_date VARCHAR(10),
    holder VARCHAR(255),
    number VARCHAR(255),
    cvv VARCHAR(4),
    brand VARCHAR(255)
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255),
    password VARCHAR(255),
    confirm_password VARCHAR(255)
);
```


## Aprendizados

Consegui extrair bastante conhecimento acerca de autenticação e autorização fazendo esse teste.

Também pude ter mais contato diretamente com o Flask, visto que tinha utilizado apenas de forma superficial.


## Melhorias

Poderia, caso o projeto ganhasse uma extensão maior, utilizar arquitetura limpa para ele.

Faria a criação de um front-end.

Melhoraria as validações realizadas nos métodos de cartão de crédito, para ganhar mais segurança nisso.

Faria uma refatoração no retorno do número do cartão, visto que está trazendo todo um hash feito para deixar ele criptografado na base.

Faria um diagrama de arquitetura, para melhorar a visualização

Faria testes end2end usando Selenium, pois por conta do tempo não consegui implementar, apenas testes unitários e de integração.

Faria a implementação de uma ferramenta de monitoramente e observabilidade como o new relic, para visualizar e armazanar os logs que foram adicionados na aplicação.

Esqueci de adicionar a validação de data menor que a data atual no fluxo de criação, mas está implementado.


## Autores

- [@luansantosdevpy](https://www.github.com/luansantosdevpy)


## Licença

[MIT](https://choosealicense.com/licenses/mit/)

