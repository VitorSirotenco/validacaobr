from cpf_cnpj import Documento


exemplo_cpf = '43085951008'
exemplo_cnpj = '35379838000112'
cnpj_um = Documento.cria_documento(exemplo_cnpj)
cpf_um = Documento.cria_documento(exemplo_cpf)
print(cnpj_um)
print(cpf_um)




