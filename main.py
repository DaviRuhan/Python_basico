'''
Autor: Davi Ruhan
Data: 02/10/24
Versão: 1.0

# ------------------------- Aula print------------------------------------

print("Ola")
print('Que dia é hoje')
print('Tudo bem?')


# --------------------------Aula variaveis------------------------------------

y = 'Olá'
print(y)

x = 2
print(x + x)


# ----------------------Aula modificação de dados--------------------------------

x = str(3)
y = int(4)
z = float(5)

print(x + x)
print(y + y)
print(z + z)


#-----------------------------Aula input-----------------------------------

nome = input('Qual é o seu nome: ')
idade = input('Qual é a sua idade: ')
idade = str(idade)
cidade = input('Onde você mora: ')

print( 'O ' + nome + ' tem ' + idade + ' anos de idade e mora em ' + cidade + '.')

#-------------------------Aula idade com input----------------------------------------

ano_nascimento = input('Em que ano você nasceu? ')
idade = 2024 - int(ano_nascimento)

print(idade)


#------------------------------Aula slice---------------------------------------

fruta = 'Abacate'
#index 0123456
print(fruta[6])
print(fruta[2:6])
print(fruta[-1])

valor = 99.75
valor = str(valor)
#index 01234
print(valor[3:5])



#------------------------------Aula formated strings---------------------------------------

nome = 'Marcos'
sobrenome = 'Silva'
profissao = 'Programador'

texto = 'O ' + nome + ' ' + sobrenome + ' é um excelente ' +  '[' + profissao + ']'
print(texto)

texto2 = f'O {nome} {sobrenome} é um excelente [{profissao}]'
print(texto2)



#------------------------------Aula metodos para strings---------------------------------------

mensagem = '         Eu adoro comida Caseira'
print(mensagem.strip())



#------------------------------Aula operações matematicas---------------------------------------

calculo = 2 ** 3 + 4

print(calculo)

#Parenteses
#Exponenciais
#Multiplicação e Divisão
#Adição e Subtração



#------------------------------Aula operadores de comparação------------------------------------

operadores = 10 >= 10
print(operadores)

# == Equal
# != Not Equal
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to



#------------------------------Aula operadores de atribuição-----------------------------------

x = 10
#x = x + 5
#x += 5
#x -= 5
#x *= 5
#x /= 5
x %= 4

print(x)

#------------------------------Aula if, else-----------------------------------

velocidade = 40

if velocidade > 110:
  print('Acima da velocidade permitida')
  print('Favor reduzir a sua velocidade')
elif velocidade < 60:
  print('Favor dirigir acima de 80Km/h')
else:
  print('Velocidade OK')


#------------------------------Aula operadores logicos-----------------------------------

renda_acima_5mil = False
nome_limpo = False

if renda_acima_5mil or nome_limpo:
  print('Financiamento Aprovado')
else:
  print('Financiamento Negado')



#------------------------------Aula multiplos operadores-----------------------------------

valor = 20

if 20 >= valor < 40:
  print('Produto foi aceito')
else:
  print('Produto não aceito')



#------------------------------Aula for looping-----------------------------------

# imprimir de 1 a 5

for numero in range(1, 20, 3):
  print(numero)


palavra = 'Ablablue'

for letra in palavra:
  print(f' {letra} esta dentro da palavra {palavra}')


# Enviar um email com os detalhes da compra online (Maximo 3 tentativas) para compras confirmadas.

compra_confirmada = True
dados_compra = 'Compra no valor de R$12.50 e entrega confirmada'

for enviar in range(3):
  if compra_confirmada:
    print(dados_compra)
    print('Detalhes enviados para o seu email')
    break
else:
  print('Falha na compra')



#------------------------------Aula nested loops-----------------------------------
# Outer loop
# Inner loop

for numero1 in range(1, 6):
  print('Produto ' + str(numero1))
  for numero2 in range(11):
    print(numero1, numero2)


#Modificar FANTASTICO para F A N T A S T I C O

palavra = 'FANTASTICO'

for spaco in palavra:
  print(f' {spaco}' , end='')


#------------------------------Aula criando um retangulo-----------------------------------

linhas = 6
colunas = 6
simbolo = '#'

for l in range(linhas):
  for c in range(colunas):
    print(simbolo, end='')
  print()


#------------------------------Aula while loop-----------------------------------

# Excelente para loops depententes de uma condição.
# Criar uma promoção para um produto no valor de R$100.

valor = 100
dia = 0

while valor > 20:
  dia += 1
  print(f' No dia {dia} o produto vai ser vendido por R${valor}')
  valor -= 5


#------------------------------Aula condições-----------------------------------

idade = 11

resultado = 'Voto Permitido' if idade >= 16 else 'Voto não Permitido'

print(resultado)


#------------------------------Aula While loop-----------------------------------

# Excelente para loops depententes de uma condição.
# Publicar um produto com comissão de 10% se for acima de R$20

valor = int(input('Digite o valor do seu Produto: '))

while valor > 20:
  valor = (valor * 0.10) + valor
  print(f'O valor final do seu produto será de R${valor}')
  break


#---------------------------Aula Funções-----------------------------------

def boas_vindas():
  print('Olá Marcos!')
  print('Temos 5 laptops em estoque')


boas_vindas()



def somar_dois_numeros():
  numero1 = 10
  numero2 = 5
  resultado = numero1 + numero2
  print(resultado)


def somar_dois_numeros1():
  numero1 = 1
  numero2 = 2
  resultado = numero1 + numero2
  print(resultado)

somar_dois_numeros()
somar_dois_numeros1()



def boas_vindas(nome, quantidade):
  print(f'Olá {nome}.')
  print(f'Temos {str(quantidade)} laptops em estoque')

boas_vindas(input('Qual é o seu nome? '), input('Qual é a quantidade? '))

#---------------------------Aula Print ou Return-----------------------------------
def client1(nome):
  print(f'Olá {nome}')

def client2(nome):
  return f'Olá {nome}'

x = client1('Maria')
y = client2('José')

print(x, y)


#---------------------------Aula Vários argumentos xargs com números-----------------------

#Criar uma função que soma vários números.

def soma(*numeros):
  resultado = 0
  for num in numeros:
    resultado += num
  return resultado


x = soma(2,3,4,7)
print(x)



#---------------------------Aula Vários argumentos xargs nomeando-----------------------

def agencia(**carro):
  return carro


print (agencia(marca='Gol', cor='Branco', motor=1.0, placa=1234))
print (agencia(marca='Gol', cor='Azul', motor=1.0))
print (agencia(marca='Gol', cor='Preto'))


#---------------------------Aula Importando um módulo-----------------------------------

#Qual é o numero fatorial de 4
# 4 * 3 * 2 * 1 = 24
import math

print(math.factorial(40))

fatorial = 4 * 3 * 2 * 1
print(fatorial)

print(math.ceil(2.7))


#---------------------------Aula Listas------------------------------------------------

cidade1 = 'Rio de Janeiro'
cidade2 = 'São Paulo'
cidade3 = 'Salvador'
cidade4 = 'Goiania'

cidades = [cidade1, cidade2, cidade3, cidade4]

#cidades.append('Santa Catarina')
#cidades.remove('Salvador')
#cidades.insert(1, 'Santa Catarina')
#cidades.pop(0)
cidades.sort()

print(cidades)


#---------------------------Aula Concatenar Listas------------------------------------------

numeros = [2, 3, 4, 5]
letras = ['a', 'b', 'c', 'd']

numeros.extend(letras)
print(numeros)


itens = [['item1', 'item2'], ['item3', 'item4']]

print(itens[1][0])


#---------------------------Aula Extraindo variáveis de listas--------------------------------

produtos = ['arroz', 'feijão', 'laranja', 'banana', 5, 6, 7, 8]

item1, item2, *outros, item8  = produtos

print(item1)
print(item2)
print(item8)
print(outros)



#---------------------------Aula Looping dentro de uma lista--------------------------------

valores = [50, 80, 110, 150, 170]

for x in valores:
  print(f'O valor final de R${x}.')



#---------------------------Aula Verificando itens em uma lista-----------------------------

cor_cliente = input('Digite a cor desejada: ')
cores = ['amarelo', 'verde', 'azul', 'vermelho']

if cor_cliente.lower() in cores:
  print('Em estoque')
else:
  print('Não temos em estoque')



#---------------------------Aula Agregando duas listas com o Zip-----------------------------

cores = ['amarelo', 'verde', 'azul', 'vermelho']
valores = [10, 20, 30, 40]

duas_listas = zip(cores, valores)
print(list(duas_listas))



#---------------------------Aula Input em uma lista--------------------------------

frutas_usuario = input('Digite o nome das frutas separados por virgula: ')

frutas_lista = frutas_usuario.split(', ')

print(frutas_lista)



#---------------------------Aula Tuples--------------------------------
#Não pode alterar os itens

cores_list = ['amarelo', 'verde', 'azul', 'vermelho']
cores_tuple = ('amarelo', 'verde', 'azul', 'vermelho')

print(type(cores_list))
print(type(cores_tuple))

duas_listas = cores_list * 2
print(duas_listas)
cores_list.append('Roxo')
print(cores_list)


#---------------------------Aula Arrays--------------------------------
from array import array


letras = ['a', 'b', 'c', 'd']
numeros_i = [10, 20, 30, 40]
numeros_f = [1.2, 2.2, 3.2]

print(letras)
print(numeros_i)
print(numeros_f)
print()

letras = array('u', ['a', 'b', 'c', 'd'])
numeros_i = array('i', [10, 20, 30, 40])
numeros_f = array('f', [1.2, 2.2, 3.2])

print(letras)
print(numeros_i)
print(numeros_f)



#---------------------------------Aula Sets------------------------------------
#Similar a listas
#Evita itens duplicados
#Não utiliza index

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) # Union
print(num1 - num2) # Difference
print(num1 ^ num2) # Symmetric Difference
print(num1 & num2) # And

print(len(num1))



#---------------------------------Aula Funções em Set-----------------------------------

s1 = {1, 2, 3, 4, 5, 6, 1, 2}
s1.update({7, 8, 9, 10})
s1.remove(10)
s1.discard(90)

print(s1)



#----------------------------------Aula Sets com String----------------------------------

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

set4 = set1.union(set2)
set5 = set1.difference(set3)
set6 = set1.intersection(set2)
set7 = set1.symmetric_difference(set3)

print(set4)
print(set5)
print(set6)
print(set7)



#----------------------------------Aula Dicionários----------------------------------
#Utiliza index no formato de Keys e Values
#Aceita string, integer, float, boolean...

aluno = {
  'nome': 'Ana', 
  'idade': 16, 
  'nota_final': 'A', 
  'aprovação': True, 
  'Materias': ['Fisica', 'Matematica', 'Ingles']
}

#aluno['nome'] = 'José'
#aluno.update({'nome': 'José', 'nota_final': 'B', 'endereco': 'Rua A'})

#del aluno['idade']

#print(aluno)
#print(aluno.get('nota_final', 'Não existe'))
#print(len(aluno))
#print(aluno.items())
#print(aluno.keys())
#print(aluno.values())


#for keys, values in aluno.items():
#  print(keys, values)



#----------------------------------Aula Lambda Function----------------------------------
#É uma função (pequena) sem nome
#Pode ter vários argumentos mas somente 1 expressão
#Muito utilizada dentro de outras funções
#Código mais 'clean'

def somar(x):
  func2 = lambda x: x + 10
  return func2(x) * 4

print(somar(2))

#somar10 = lambda x, y: x + y + 10
#print(somar10(2, 4))



#---------------------------Aula Map Function----------------------------------
#Muito utilizado com listas
#Aplicar uma função a um Iterable, por item. (list, tuple, dic, etc.)

lista1 = [1, 2, 3, 4]

#def multi(x):
#  return x * 2

#lista2 = map(lambda x: x * 2, lista1)

print(list(map(lambda x: x * 2, lista1)))



#---------------------------Aula Filter Function----------------------------------
#Aplicar uma função a um Iterable, filtrando os items. (list, tuple, dic, etc.)

valores = [10, 12, 34, 44, 57]

#def remover20(x):
#  return x > 20

#print(list(filter(remover20, valores)))

print(list(filter(lambda x: x > 20, valores)))



#---------------------------Aula List Comprehension----------------------------------
#Mais simples de se escrever
#Utilizado quando você precisa criar uma nova lista a partir de uma existente
#[expressão for iten in itens]

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']

#frutas2 = []

#for item in frutas1:
#  if 'b' in item:
#    frutas2.append(item)

frutas2 = [item for item in frutas1 if 'n' in item]

print(frutas2)



#valores = []

#for x in range(6):
#  valores.append(x * 10)

#print(valores)

valores = [x * 10 for x in range(6)]
print(valores)



#---------------------------Aula Generator Expressions----------------------------------
#Uma forma mais rápida para listas, dicionários e etc.
#Menos memória alocada
#Valores em bytes

from sys import getsizeof

numeros = [x * 10 for x in range(10000000)] #Gasta muita memoria
print(type(numeros))

print(getsizeof(numeros))

print('------------')

numeros = (x * 10 for x in range(10000000))
print(type(numeros))
print(getsizeof(numeros))



#---------------------------Aula Erros----------------------------------
#Excelente para testes
#Não realiza o 'stop' no programa
#Mensagens customizadas quando encontra um erro


try:
  letras = ['a', 'b', 'c']
  print(letras[3])
except IndexError:
  print('Index não exite')


try:
  valor = int(input('Digite o valor do seu produto: '))
  print(valor)
except ValueError:
  print('Favor digitar apenas numeros!')
finally:
  print('Código OK')

#else:
#  print('Usuário digitou um valor correto')
#  resultado = valor * 2
#  print(resultado)  

print('Mais código abaixo')



#---------------------------Aula Classes----------------------------------
#Utilizadas para criar objetos (instances)
#Objetos são partes dentro de uma class (instancias)
#Classes são utilizadas para agrupar dados e funções, podendo reutilizar
#Class: Frutas
#Objects: Abacate, Banana...

from datetime import datetime

#criar classe
class Funcionarios:

  def __init__(self, nome, sobrenome, ano_nascimento):
    self.nome = nome
    self.sobrenome = sobrenome
    self.ano_nascimento = ano_nascimento
    
  def nome_completo(self):
    return self.nome + ' ' + self.sobrenome

  def idade_funcionario(self):
    ano_atual = datetime.now().year
    self.ano_nascimento = int(ano_atual - self.ano_nascimento)
    return self.ano_nascimento


#criar objeto
usuario1 = Funcionarios('Elena', 'Cabral', 2009)
usuario2 = Funcionarios('Carol', 'Silva', 2005)


print(usuario1.nome_completo())
print(Funcionarios.nome_completo(usuario1))
print(Funcionarios.idade_funcionario(usuario1))

'''




