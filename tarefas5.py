listal = ['Dieimes', 'Nunes','Souza','Caio','Luana']
print(type(listal))
print(len(listal))
print(listal[4])

lista2 = listal *2
print(lista2)

listal.remove("Caio")
print(listal)

for listageral in listal:
    print(listageral)