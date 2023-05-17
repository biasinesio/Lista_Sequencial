#LISTA ESTRUTUTA DE DECISÃO

#1)Solicite ao usuário um valor numérico, inteiro ou real, e verifique se ele é maior ou
#menor que 10. O programa deve escrever a mensagem correspondente (maior ou
#menor) e informar o valor digitado pelo usuário.

valor= float(input("Digite um valor: "))

if valor > 10:
    print("\nO valor é maior que 10.")
else:
    print ("\nO valor é menor que 10.")
    print (f"\nO valor digitado foi {valor}:\n")


#2. Solicite ao usuário um valor numérico, inteiro ou real, e escrever se é positivo ou
#negativo (considere o valor zero como positivo).

valor= float(input("Digite um valor: "))

if valor >= 0:
    print("\nO valor é positivo.")
else:
    print("\nO valor é negativo.")


#3. As maçãs custam 1,30 cada, se forem compradas menos de uma dúzia, e 1,00 se
#forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs
#compradas, calcule e escreva o custo total da compra.

n_maça= int(input("\nDigite a quantidade de maçãs: "))

if n_maça <12:
    custo =  n_maça* 1.30
else:
    custo = n_maça* 1.0
print(f"\nO valor total da compra é: {custo :.2f} \n")


#4. Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples
#e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que
#nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

nota1 = float(input("Digite sua 1º nota: "))
nota2 = float(input("Digite sua 2 nota:º "))
media = (nota1 + nota2)/2

if media >=6:
    print("\n Parabéns! Você foi aprovado.")
else:
    print("\nVocê foi reprovado")
print(f"\nSua média foi: {media :.2} \n")


#5. Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior
#deles.

v1= float(input("Digite o primeiro número: "))
v2= float(input("Digite o segundo número: "))

if v1 > v2:
    print(v1 ,"é maior que", v2)
else:
    print(v2, "é maior que", v1)


#6. Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em
#ordem crescente.

v1= float(input("\nDigite o 1º número: "))
v2= float(input("Digite o 2º número: "))

if v1 > v2:
    print("\nA ordem crescente é: ",v2 , v1)
else:
    print("\nA ordem crescente é: ",v1 , v2)


#7. Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após,
#calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também
#testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo',
#senão escrever a mensagem 'Saldo Negativo'.

n_conta = input("\nDigite o número da conta: ")
saldo = float(input("Digite o saldo da conta: "))
debito = float(input("Digite o débito da conta: "))
credito = float(input("Digite o crédito da conta: "))
saldo_atual = saldo - debito + credito

if saldo_atual >= 0:
    print("\nSaldo Positivo")
    print("\nSaldo atual:", saldo_atual)
else:
    print("\nSaldo Negativo")
    print("\nSaldo atual:", saldo_atual)


#8. Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em
#estoque e quantidade mínima em estoque de um produto. Calcular e escrever a
#quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2).
#Se a quantidade em estoque for maior ou igual a quantidade média, escrever a
#mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar compra'.

q_atual = int(input("\nDigite a quantidade atual do produto em estoque: "))
q_max = int(input("Digite a quantidade máxima do produto em estoque: "))
q_min = int(input("Digite a quantidade mínima do produto em estoque: "))

q_média = (q_max + q_min) / 2
if q_atual >= q_média:
    print("\nNão efetuar compra.")
else:
    print("\nEfetuar compra.")


#9. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina
#ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à
#tabela abaixo:
#Média de Aproveitamento Conceito
#Entre 9.0 e 10.0 A
#Entre 7.5 e 9.0 B
#Entre 6.0 e 7.5 C
#Entre 4.0 e 6.0 D
#Entre 4.0 e zero E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a
#mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o
#conceito for D ou E.

nota1 = float(input("\nDigite a nota da 1º avaliação: "))
nota2 = float(input("Digite a nota da 2º avaliação: "))
media = (nota1 + nota2) / 2

if media >= 9:
    conceito = "A"
elif media >= 7.5:
    conceito = "B"
elif media >= 6:
    conceito = "C"
elif media >= 4:
    conceito = "D"
else:
    conceito = "E"

print("\n1º nota:", nota1)
print("2º nota:", nota2)
print("Média:", media)
print("Conceito:", conceito)

if conceito in ("A", "B", "C"):
    print("\n>>APROVADO<<\n")
else:
    print("\n>>REPROVADO<<\n")