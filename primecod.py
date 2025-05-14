# códigos e funções para prática em python - Meus estudos.

# detalhes sobre strings - aspas

mensagem = 'Eu gosto muito pizza de calabresa'

# indexação e fatiamento

print (mensagem[0:32])

# Métodos comuns para Strings

print (mensagem.upper())
print (mensagem.lower())
print (mensagem.strip())
print (mensagem.replace('gosto', 'amo',))
print (mensagem.split())

# formatação de f-string - teste com a funçaõ input

nome = input ("por favor digite seu nome: ")
peso = input ("por favor digite seu peso: ")
idade = input ("por favor digite sua idade: ")
# o 'f' disponibiliza voce por uma variavel dentro de chaves {}
print (f'olá! {nome}, é um grande prazer te conhecer.')
print (f'''certo, sabendo que você pesa {peso}kg e sua idade é {idade}, 
poderei analisar melhor seu perfil {nome.strip()}.''')

# escape sequence

mensagem1 = 'aprendendo python de \nforma simples'
# \n <--- pula uma linha, sem a necessidade de por '''.
mensagem2 = 'Coluna1\tColuna2\tColuna3'
#  \t <--- adiciona uma tabulação.
print (mensagem1)
print (mensagem2)

# caso queira alguma palavra em aspas, precisa por sempre \ barras investidas, uma antes da primeira aspa e uma antes da prox aspa

mensagem3 = 'aprender \'python\' é muito divertido'
print (mensagem3)

# Tabulações e unicode com Strings

mensagem4 = 'nome:\tSarah Gonzalez\nIdade:\t18\nPeso:\t60.3'
print (mensagem4)

# caracteres unicode

mensagem5= 'Coração: \u2764'

print (mensagem5)