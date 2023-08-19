dados_cliente = {
    "Nome": "João Paulo",
    "Endereco": "Rua Eugenio, 23",
    "Telefone": "988179995"
    }

print (dados_cliente['Nome'])
dados_cliente["Cidade"] = "Faxinal"
print (dados_cliente)
dados_cliente.pop("Telefone")