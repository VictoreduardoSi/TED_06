#Questão de número 6
convidados =["Casimito", "Zezo o Príncipe dos teclados", "Messias Rafael", "Edson Luiz", "Michele Kelly" ]
for convidado in convidados:
 print("Olá,", convidado + "!", "Gostaria de Convidar você para um jantar comemorativo dos meus 18 anos no dia 17/02/2023, será na minha casa no próximo sábado")

convidados.remove ("Edson Luiz")
print("infelizmente,", convidados[2], "não poderá comparecer ao jantar.")
convidados[2] = "Mateus André"
convidados.append("Samuel Vinicius")
for convidado in convidados:
    print("Olá,", convidado + "!", "Gostaria de Convidar você para um jantar comemorativo dos meus 18 anos no dia 17/02/2023, será na minha casa no próximo sábado")



