usuario=[]
nome=str(input("insra seu nome"))
print("\n")
email=str(input("insira seu email"))
print("\n")
cpf=int(input("insira seu cpf"))
print("\n")
cnpj=int(input("insira seu cnpj"))
print("\n")
telefone=input("insira seu telefone")
print("\n")
cep=input("insira seu cep")
print("\n")
logradouro=input("insira o logradouro")
print("\n")
numero=input("insira o numero")
print("\n")
bairro=input("insira o Bairro")
print("\n")
cidade=input("insira a cidade")
print("\n")
estado=input("insira o estado")


usuario={
    "nome":nome,
    "email":email,
    "cpf":cpf,
    "cnpj":cnpj,
    "tel":telefone,
    "cep":cep,
    "logradouro":logradouro,
    "numero":numero,
    "Bairro":bairro,
    "Cidade":cidade,
    "Estado":estado,

}

print(usuario)
opc=str(input("\n insira qual campo deseja remover(nome,email,cpf,cnpj,tel,cep,logradouro,\n,numero,Bairro,Cidade,Estado) \n"))
#remoção de items
def remocao(opc):
    usuario.pop(opc)
remocao(opc)
print(usuario)



