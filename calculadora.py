entrada_1 = float(input('Informe o primeiro valor: '))
entrada_2 = float(input('Informe o segundo valor: '))

soma = entrada_1 + entrada_2
subtracao = entrada_1 - entrada_2
multiplicacao = entrada_1 * entrada_2
divisao =  entrada_1 / entrada_2

print('A soma dos valores é:', soma)
print('A subtração dos valores é:', subtracao)
print('A multiplicação dos valores é:', multiplicacao)
print('A divisão dos valores é:', divisao)

tabuada_1 = input('Deseja gerar a tabuada do primeiro valor? (Sim / Nao)')

if tabuada_1.lower() == 'sim':
  for i in range(1,11):
    valor = entrada_1 * i
    print(entrada_1,'x',i,'=',valor)

tabuada_2 = input('Deseja gerar a tabuada do segundo valor? (Sim / Nao)')

if tabuada_2.lower() == 'sim':
  for i in range(1,11):
    valor = entrada_2 * i
    print(entrada_2,'x',i,'=',valor)
