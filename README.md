# Resumo do Projeto
Dois endpoints foram desenvolvidos usando Django.

O primeiro é para o cadastro de novos usuários, com nome, senha e data de nascimento. Caso a senha não seja fornecida, será gerada pelo próprio sistema e guardada no banco de dados.

O segundo é para a consulta desse banco de dados em três formatos:
- CSV
- JSON
- XLSX

## Lista de dependências
- asgiref 3.5.2
- Django 4.1.2
- sqlparse 0.4.3
- tzdata 2022.5
- xlwt 1.3.0