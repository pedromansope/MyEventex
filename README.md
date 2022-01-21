# Eventex

Sistema de eventos para desenvolvimento e estudo com Python e Django.

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.+
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env

```console
git clone git@github.com:/pedromansope/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY.
4. Defina DEBUG=False.
5. Configure o serviço de e-mail, referente ao formulário.

```console
heroku create yourinstance
heroku config:push
heroku config:set SECRET_KEY=defineyoursecretkey
heroku config:set DEBUG=False
# E-mail config
git push heroku master --force
```