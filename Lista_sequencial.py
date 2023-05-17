#Lista de exercícios - Estrutura Sequencial:

#1. Faça um programa que converta metros para centímetros.

metros = float(input( "Digite o valor em metros a ser convertido em centímetros: "))
cm = metros*100
print("O valor em centímetros é de {}".format(cm))

#2. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = float(input("Digite o raio do círculo: "))
area = 3.14*raio**2
print("A área do círculo é de: {}".format(area))


#3. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro
#desta área para o usuário.

altura = float(input("Digite o valor da altura do quadrado: "))
base = float(input("Digite o valor da base do quadrado: "))
area = base*altura*2
print("O dobro da  área do quadrado é de: {}".format(area))

#4. Faça um Programa que calcule a área de um triângulo, em seguida mostre o dobro
altura = float(input("Digite o valor da altura do Triângulo: "))
base = float(input("Digite o valor da base do Triângulo: "))
area = base*altura/2
area2= area*2
print ("O valor do dobro da área do triângulo é: {}".format(area2))


#4. Faça um Programa que pergunte quanto você ganha por hora e o número de horas
#trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

#!!!!ESTOU LEVANDO EM CONSIDERAÇÃO QUE A PESSOA TRABALHA 30 DIAS NO MÊS
salario = float(input("No seu atual emprego quanto você ganha por hora? "))
hora = float(input("E quantas horas você trabalha por dia?"))
total = hora*salario*30
print ("O valor total do seu salário é: {}".format(total))

#5. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre
#a temperatura em graus Celsius.
#1. C = 5 * ((F-32) / 9).

fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
celsius = (fahrenheit - 32) / 9
print ("A temperatura em graus Celsius é: {}".format(celsius))

#6. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em
#graus Fahrenheit.

celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = (celsius * 9) + 32
print ("A temperatura em graus Fahrenheit é: {}".format(fahrenheit))

#7. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#1. o produto do dobro do primeiro com metade do segundo .
#2. a soma do triplo do primeiro com o terceiro.
#3. o terceiro elevado ao cubo.

n1 = float(input("Digite um número inteiro: "))
n2 = float(input("Digite mais um número inteiro: "))
n3 = float(input("Digite um número real: "))
resultado1 = (n1 * 2) * (n2/2)
resultado2 = (n1 * 3) + n3
resultado3 = n3 **3
print ("O produto entre o dobro do primerio número e a metade do segundo número:4",resultado1 )
print ("A soma entre o triplo do primeiro número e o terceiro número:",resultado2)
print ("O terceiro número elevado ao cubo:",resultado3)

#8. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que
#calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Digite sua altura: "))
calculo_peso = (72.7 * altura) - 58
print ("seu peso ideial é: {}".format(calculo_peso))

#9. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que
#calcule seu peso ideal, utilizando as seguintes fórmulas:
#1. Para homens: (72.7*h) - 58
#2. Para mulheres: (62.1*h) - 44.7

altura = float(input("Digite sua altura: "))
homem = (72.7 * altura) - 58
mulher = (62.1 * altura) - 44.7
print ("Seu peso ideal se você for Homem: ", homem, "\nSeu peso ideial se você for Mulher:", mulher)