Passo a passo para utilizar essa API:

1.Entrar na pasta raiz através do CD:
cd /home/...

2.Utilize o comando abaixo para rodar a VENV (ambiente virtul):
source .venv/bin/activate

3.Criar um usuario no framework Django com o comando abaixo:
python manage.py createsuperuser

4.Rodar o servidor com o comando abaixo:
python manage.py runserver

Em "127.0.0.1:8000/admin" você poderá fazer o login com o usuario criado e cadastrar novos produtos.

Não é permitido codigos de barras ou codigos do produto duplicado. Para alterar, vá em models no app e delete "unique=True"
o Grupo de um produto é obrigatório, mas como padrão ele vem "0 - Geral"
