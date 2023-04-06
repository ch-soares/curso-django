# Curso de django: DevPro

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

#### Crie e ative o ambiente virtual:

```commandline
python -m venv .venv
source .venv/bin/activate
```

#### Realize as migrações para gerar esquema de banco de dados:

```commandline
python manage.py migrate
```

#### Crie um usuário para acessar a página de administração do Django:

```commandline
python manage.py createsuperuser
```

#### Rodando o servidor local:

```commandline
python manage.py runserver
```

# O aprendizado

## Um resumo

#### No atual estágio da minha vida, tenho convicção que posso aprender qualquer coisa. O tempo e a qualidade do aprendizado, entretanto, decorrerá da vontade e do foco colocado no conhecimento que se pretende adquirir. No que se refere à programação ou desenvolvimento de software, objeto destas minhas linhas, estou certo que meu foco e minha vontade cresce a cada dia. Uma das razões para este fato decorre da paixão que possuo em resolver problemas das pessoas por meio da tecnologia. Aprender uma tecnologia nova é sempre motivador! Neste sentido, posso dar certeza que consigo aprender qualquer ferramenta que vise resolver problemas.

## Sobre este projeto

### Primeira parte: Afiando o machado

#### Tal como faz um bom chefe de cozinha, que primeiro afia as facas, organiza as panelas, os temperos etc para executar o prato; assim se deve fazer um bom desenvolvedor de software.

#### Fi feito uso de bibliotecas e ferramentas que auxiliem o desenvolvimento, dando agilidade na execução, bem como ajuda na manutenção do sistema, uma vez que são tecnologias consolidadas e com extensa documentação disponível. Vamos a elas:

| Biblioteca / Ferramenta  | Resumo do que faz                                                                                                                                          |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Pytest-django            | Plugin para pytest que fornece um conjunto de ferramentas úteis para testar aplicativos e projetos Django.                                                 |
| Python-decouple          | Configura dados sensíveis da aplicação, como: SECRET_KEY, ALLOWED_HOSTS e DEBUG; de modo que estes parâmetros não sejam mostrados em produção.             |  
| dj-database-url          | retorna um dicionário de conexão de banco de dados Django, preenchido com todos os dados especificados em sua URL.                                         |
| django-s3-folder-storage | Extensão rápida do S3BotoStorage do django-storages para permitir pastas separadas para mídia carregada e estática dentro de um bucket S3.                 |
| collectfast              | personaliza o comando interno collectstatic, adicionando diferentes otimizações para tornar o upload de grandes quantidades de arquivos muito mais rápido. |
| flake8                   | Ajusta o código de acordo com a pep8.                                                                                                                      |
| pytest-cov               | produz relatórios de cobertura de testes.                                                                                                                  |
| codecov                  | Gera relatório de cobertura com base no pytest-cov.                                                                                                        |
| django-debug-toolbar     | Cria uma barra de ferramentas de depuração do Django no browser de forma interativa e intuitiva.                                                           |
| sentry-sdk               | Interage com a aplicação e fornece respostas para os eventuais problemas que a aplicação apresentar.                                                       |
