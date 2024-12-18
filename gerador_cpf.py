import random
import time
run = 1
while run == 1:
    inp = input('quantos cpfs deseja gerar? ')
    if not  inp.isdigit():
        print('Digite apenas números')
        continue
    elif int(inp) == 0:
        print('Digite um número maior que 0')
        continue
    else:
        x = int(inp)

    for _ in range(x):
        
        cpf1 = ''
        for i in range(9):
            cpf1 += str(random.randint(0, 9))  
        
        i = 10
        soma = 0
        for digito in cpf1:
            mt = (int(digito) * i)
            i -= 1
            soma = soma + mt

        resultado1 = soma * 10
        resultado2 = resultado1 % 11
        
        digito1 = resultado2 if resultado2 <= 9 else 0

        cpf2 = ''.join(cpf1) + str(digito1)

        j = 11
        soma = 0
        for digito in cpf2:
            mt = (int(digito) * j)
            j -= 1
            soma = soma + mt

        resultado1 = soma * 10
        resultado2 = resultado1 % 11
        
        digito2 = resultado2 if resultado2 <= 9 else 0

        cpf_gerado = f'{cpf1}{digito1}{digito2}'
        
        lista = []
        for digito in cpf_gerado:
            lista.append(digito)

        lista.insert(3, '.')
        lista.insert(7, '.')
        lista.insert(11, '-')

        print('CPF gerado:  ', *lista, sep='')

    run = int(input('Deseja gerar mais cpfs? 1 para sim e 0 para nao: '))
    time.sleep(3)