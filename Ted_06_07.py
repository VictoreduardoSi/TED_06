#Questão de número 7
user = []
continuar = "s"
while continuar == "s":
    nome = input("Digite seu usuário:")
    idade = int(input("Digite a sua idade:"))
    email = input("Digite seu melhor email:")
    
    novo_usuario = {"nome": nome, "idade": idade,"email": email }
    user.append(novo_usuario)
    continuar = input("Deseja cadastrar outro usuário? (s/n):")
    while continuar != "s" and continuar != "n":
        continuar = input("Resposta inválida. Deseja cadastrar outro usuário? (s/n):")
        print("Usuários cadastrados:")
        for usuario in user:
            print(usuario)


