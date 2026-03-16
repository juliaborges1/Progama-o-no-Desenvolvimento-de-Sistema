#Variavel é um espaço de memoria que tem um nome e guarda algum dado do meu programma
# Aqui estamos criando uma variável chamada "numero"
# O sinal = significa atribuição (guardar um valor dentro da variável)
# Nesse caso estamos guardando o valor inteiro 5
numero = 5


#Expressao são quaisquer combinações de valores , variaveis e operadores
# Aqui criamos outra variável chamada "resultado"
# Estamos fazendo uma expressão matemática usando a variável numero
# numero + numero + 5 significa: 5 + 5 + 5
resultado = numero + numero + 5

# Aqui temos outra expressão matemática um pouco mais complexa
# Primeiro o Python resolve o que está dentro dos parênteses (numero + numero)
# Depois multiplica por numero
# Depois soma 33
# Observação: essa variável está escrita como "resulatado" (parece um erro de digitação)
resultado = (numero*(numero + numero) + 33)

#A instrução print mostra  o programa no terminal
# A função print() serve para mostrar informações na tela do terminal
# Aqui estamos mostrando o valor que está guardado dentro da variável resultado
print(resultado)

#Precedencia de operadones
#Parenteses precendencia mais alta
# Exponenciação
# Multiplicação e a Divisão
# Adição e a Subtração
# Concatenaão de Strings

nome = ("julia")
sobrenome = ("borges")
anos = 17
print("o nome dela é", nome, sobrenome, "ela tem",anos,"anos" )


nome = ("julia")
sobrenome = ("borges")
nomeinteiro = nome+sobrenome
print(nomeinteiro)

#contatenaçao de String

nome = "julia"
sobrenome = " borges"
nomeinteiro = nome + sobrenome
print(nomeinteiro)

#multiplicaçao de Strings
string1 = 'teste ' * 3
print(string1)
