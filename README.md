# Curso de django: Python Pro

### Projeto desenvolvido no módulo de Django do site [Python Pro](https://pythonpro.com.br/)

[![Updates](https://pyup.io/repos/github/ch-soares/curso-django/shield.svg)](https://pyup.io/repos/github/ch-soares/curso-django/)
[![Python 3](https://pyup.io/repos/github/ch-soares/curso-django/python-3-shield.svg)](https://pyup.io/repos/github/ch-soares/curso-django/)
[![codecov](https://codecov.io/gh/ch-soares/curso-django/branch/main/graph/badge.svg?token=K7IYCXB0SR)](https://codecov.io/gh/ch-soares/curso-django)
[![CI](https://github.com/ch-soares/curso-django/actions/workflows/.deploy.yml/badge.svg)](https://github.com/ch-soares/curso-django/actions/workflows/.deploy.yml)

## Para instalar localmente:

Supondo que tenha Git e Python (versao: > 3.11) devidamente instalados.

```
git clone https://github.com/ch-soares/curso-django.git
cd curso-django
cp contrib/env-sample .env
python -m pip install pipenv
pipenv install -d
```

Crie e ative o ambiente virtual:

Os comandos são para Linux. Para outros sistemas operacionais, podem sofrer leves mudanças. No caso do Windows, sabe-se que ao invés de "bin", usa-se "scripts".
```commandline
python -m venv .venv
source .venv/bin/activate
```

Realize as migrações para gerar esquema de banco de dados:

```commandline
python manage.py migrate
```

Crie um usuário para acessar a página de administração do Django:

```commandline
python manage.py createsuperuser
```

Rodando o servidor local:

```commandline
python manage.py runserver
```

Se desejar executar o seu ambiente de desenvolvimento usando postgres, pode adicionar ao .env:

```commandline
DATABASE_URL=postgres://postgres:pass@localhost:5432/postgres
```

# Aprendizado

>>No atual estágio da minha vida, tenho convicção que posso aprender qualquer coisa. O tempo e a qualidade do aprendizado, entretanto, decorrerá da vontade e do foco colocado no conhecimento que se pretende adquirir. No que se refere à desenvolvimento de software, objeto destas linhas, estou certo que o meu foco e minha vontade crescem a cada dia. Uma das razões para este fato decorre da paixão que possuo em resolver problemas das pessoas por meio da tecnologia. Aprender uma tecnologia nova é sempre motivador! Neste sentido, posso afirmar, com segurança, que consigo aprender qualquer ferramenta que vise resolver problemas.

## O projeto

- ### Afiando o machado

    >Tal como faz um bom lenhador, que afia bem o machado antes de começar o trabalho; ou: um bom chefe de cozinha, que primeiro afia as facas, organiza as panelas, os temperos etc para, enfim, executar o prato; assim se deve fazer um bom desenvolvedor de software. No caso deste profissional, deve-se ajustar o sistema, implementando uma base sólida por meio de boas práticas de desenvolvimento. 
Neste sentido, foram utilizadas bibliotecas e ferramentas a fim de auxiliar no desenvolvimento e proporcionar agilidade na execução, bem como facilitar a manutenção do sistema; uma vez que são tecnologias consolidadas e com extensa documentação disponível. Vamos à elas:

    | Biblioteca / Ferramenta                                                        | Resumo do que faz                                                                                                                                                     |
    |--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | [Pytest-django](https://pytest-django.readthedocs.io/en/latest/)               | Plugin para pytest que fornece um conjunto de ferramentas úteis para testar aplicativos e projetos Django.                                                            |
    | [Python-decouple](https://pypi.org/project/python-decouple/)                   | Configura dados sensíveis da aplicação, como: SECRET_KEY, ALLOWED_HOSTS e DEBUG, por exemplo; de modo que os dados destes parâmetros não sejam mostrados em produção. |  
    | [dj-database-url](https://pypi.org/project/dj-database-url/)                   | Retorna um dicionário de conexão de banco de dados Django, preenchido com todos os dados especificados em sua URL.                                                    |
    | [django-s3-folder-storage](https://pypi.org/project/django-s3-folder-storage/) | Extensão rápida do S3BotoStorage do django-storages para permitir pastas separadas para mídia carregada e estática dentro de um bucket S3.                            |
    | [collectfast](https://pypi.org/project/Collectfast/)                           | Personaliza o comando interno collectstatic, adicionando diferentes otimizações para tornar o upload de grandes quantidades de arquivos muito mais rápido.            |
    | [flake8](https://pypi.org/project/flake8/)                                     | Ajusta o código de acordo com a pep8.                                                                                                                                 |
    | [pytest-cov](https://pypi.org/project/pytest-cov/)                             | Produz relatórios de cobertura de testes.                                                                                                                             |
    | [codecov](https://docs.codecov.com/docs)                                       | Gera intuitivos relatórios e gráficos de cobertura com base no pytest-cov.                                                                                            |
    | [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) | Cria uma barra de ferramentas de depuração do Django no browser de forma interativa e intuitiva.                                                                      |
    | [sentry-sdk](https://docs.sentry.io/platforms/python/guides/django/)                                                                 | Interage com a aplicação e fornece respostas para os eventuais problemas que a aplicação apresentar.                                                                  

## Licença

### MIT

#### Com exceção do logotipo e a imagem do Dev Pro, que devem ser substuídos pela sua marca, usufrua de todo o resto livremente. Software Livre!

## Divirta-se!
