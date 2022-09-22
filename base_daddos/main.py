arquivo = open('telefones.csv')
dados = arquivo.read()

envios = []

cont = 0

for registro in dados.splitlines():
    
    #print('Nome: {}, telefone: {}'.format(*registro.split(',')))
    valor = '{}, {};'.format(*registro.split(','))
    envios.insert(cont, valor)
    cont += 1
    print(cont)


arquivo.close()

print(envios)

with open("dados.txt", "w") as f:
    f.write(envios + ',\n')
    

print(valor)
