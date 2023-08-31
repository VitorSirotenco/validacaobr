import requests

from acesso_cep import BuscaEndereco


cep = '08280160'
objeto_cep = BuscaEndereco(cep)
bairro, cidade, uf = objeto_cep.acessa_via_cep()

r = requests.get('https://viacep.com.br/ws/08280160/json/')
print(r.text)

print(bairro)
print(cidade)
print(uf)











