# APIs - são servições disponibilizados online para acessasr recusrso ou funcionalidades de alguma aplicação web

# Possue 4 partes 
# 1 - url base
    # precisar passar 1
# 2 - endpoint
    # Apos a url base 
# 3 - recurso
    # Tudo que e retornado ou enviado a uma api e considerado recurso
# 4 - verbos http
    #get-post-put-delete
# Status code 
#-----------------------------------------------

# Como usar 4 principais comando de uma api 

import requests 
from pprint import pprint

# get - obeter informa;'o de uma api 
resultado_get = requests.get("https://jsonplaceholder.typicode.com/todos/") 
#pprint(resultado_get.json())
# get com id

resultado_get_id = requests.get("https://jsonplaceholder.typicode.com/todos/2")
#pprint(resultado_get_id.json())

# post criar novo recurso 
nova_tarefa = {'completed': False,
 'title': 'Seila',
 'userId': 1}
resultado_post = requests.post("https://jsonplaceholder.typicode.com/todos/", nova_tarefa)
#pprint(resultado_post.json())

# put - alterar recurso existente  
tarefa_alterada = {'completed': False,
 'title': 'Seila32',
 'userId': 1}
resultado_put = requests.put("https://jsonplaceholder.typicode.com/todos/2", tarefa_alterada )
#pprint(resultado_put.json())

# delete - para excluir
resultado_delete =requests.delete("https://jsonplaceholder.typicode.com/todos/2")
pprint(resultado_delete.json())













