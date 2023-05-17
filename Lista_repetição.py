#Lista Estrutura de Repetição

#1. Desenvolva um programa que verifique e mostre os números entre 1.000 e 2.000 que, quando
#divididos por 11, produzam o resto igual a 5.

for número in range(1000, 2001):
    if número % 11 == 5:
        print (número)


#2. Faça um programa que mostre as tabuadas dos números de 1 a 10.

for número in range (1, 11):
    print ("\nTabuada do número" , número,":\n")
    
    for multiplicador in range (1, 11):
        produto = número * multiplicador
        print (número, "x" , multiplicador , "=", produto)
        print ()
   

#3. Armazene os nomes de alguns de seus amigos em uma lista chamada amigos. Exiba o nome de cada
#pessoa acessando cada elemento da lista um de cada vez.

amigas = ["\n1º Lara Yasmin\n", "2º Carolina Rocha\n", "3º Júlia Moraes\n", "4º Bia Sinésio\n"]

print ("\nLista de Amigas: ")
print (amigas [0])
print (amigas [1])
print (amigas [2])
print (amigas [3])


#4. Faça um programa que receba um número e que calcule e mostre a tabuada desse número.

número = int(input("Digite um número de 1 a 20: "))

print ("\nTabuada do número",":\n")

for num in range(1, 20):
    produto = número * num
    print (número, "x", num, "=", produto)

#5. Utilizando a lista do exercício anterior, exiba uma saudação ("Olá como vai você"), personalizado
#com o nome de cada amigo. A saudação deve ser a mesma, alterando apenas o nome do amigo.

amigas = [" Lara Yasmin", "Carolina Rocha", "Júlia Moraes", "Bia Sinésio"]

for amiga in amigas:
    print ("\nLista de amigas:")
    print ("\nOlá", amiga,", como vai você?\n")


#6. Seja criativo ao desenvolver este programa.
#a. Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.
#b. Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome
#personalizado.
#c. Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos
#convites. Imprima o nome das pessoas que não poderão comparecer.
#d. Modifique sua lista, substitua os desistentes por novos convidados.
#e. Exiba um novo convite para cada pessoa que continua presente em sua lista.

convidados = ["Jennifer Aniston", "Adam Sandler", "Bruna Marquezine", "Kim taehyung", "Kim bok joo"]
nao_vem = []

nao_vem.append("Jennifer Aniston\n")
convidados.remove("Jennifer Aniston")

# Novos convidados
convidados.append("Nam joo hyuk")
convidados.append("Neymar")

for convidado in convidados:
    print("\nOlá, " + convidado + "! Você está convidado(a) para um jantar na minha casa neste sábado às 20h.")
    
print("\nOs seguintes convidados não poderão comparecer:")
for ausente in nao_vem:
    print(ausente)


#7. Faça um cadastro de usuários com nome, idade e email, utilizando apenas o que você aprendeu até
#agora.

usuários = []

while True:
    nome = input("Digite o nome do usuário (ou 'sair' para encerrar o programa): ")
    if nome.lower() == "sair":
        break
    
    idade = int(input("Digite a idade do usuário: "))
    email = input("Digite o e-mail do usuário: ")
    
    usuario = {"nome": nome, "idade": idade, "email": email}
    usuários.append(usuario)
    
print("\nCadastro de usuários finalizado!")
print("\nForam cadastrados os seguintes usuários:\n")

for usuário in usuários:
    print("Nome: " + usuário["nome"])
    print("Idade: " + str(usuário["idade"]))
    print("E-mail: " + usuário["e-mail"])
    print()