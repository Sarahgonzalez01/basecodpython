# captura do valor do produto - todo esse código é para estudos do 0 em python
from base64 import a85decode

money = float(input('Digite o valor do produto: R$ '))

# calcula o valor com 10% (adicionar)

valor_adicionado= money * 1.1

print (f'O valor deste produto é: R${valor_adicionado:.2f} ') # '.2f' quantas casas esse resultado vai ter

# exibir o valor final na tela

# multiplas entradas na mesma linha de input

dados = input ('digite seu nome e idade: ').split() #Sarah 18 <-- split: separa as palavras
nome = dados[0] #o index de dados é 0 pois ele está amarzenando como um grupo
idade = dados [1] #o index de idade é 1 pois ele amarzena como um grupo

print (f'Olá, me chamo {nome.upper()} e tenho {idade} anos de idade.')

# Operadores de comparação - igual a x == y
#em strings isso funciona de forma diferente, posso por um texto e comparar se ele é igual a outro em forma de string
a = 10
b = 35
print (a==b) # '==' <--- igual a: boolean (true or false)

# Operadores de comparação - Diferente de x != y

a2= 21
b2 = 41
print (a2!=b2) # '!=' <--- diferente de: boolean (true or false)

# Operadores de comparação - Maior que x > y

a3 = 32
b3= 67
print (a3>b3) # '>' <--- maior que: boolean (true or false)

# Operadores de comparação - menor que x < y

a4 =23
b4= 34
print (a4<b4)   #'<' <--- menor que: boolean (true or false)

# Operadores de comparação - maior ou igual que x >= y

a5= 45
b5=  12
print (a5>=b5) #'>=' maior ou igual: boolean (true or false)

# Operadores de comparação - menor ou igual que x <= y

a6 = 45
b6 = 12
print(a6 >= b6)  # '<=' maior ou igual: boolean (true or false)