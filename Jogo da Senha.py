import random

# Gerar um número aleatório entre 11 e 99
numero_sorteado = random.randint(11, 99)
# Lista de Distritos
distritos = ["CityCenter", "Westbrook", "Heywood", "Pacifica", "SantoDomingo", "Watson", "TheBadlands", "Dogtown"]

# Definir as regras de validação de senha
regras = [
    lambda x: len(x) >= 5,  # Regra 1: Comprimento mínimo
    lambda x: any(c.isupper() for c in x),  # Regra 2: Letra maiúscula
    lambda x: any(c.isdigit() for c in x),  # Regra 3: Número
    lambda x: any(c in "!@#$%^&*()_+-=[]{}|;':\",./<>?" for c in x),  # Regra 4: Caractere especial
    lambda x: sum(int(d) for d in x if d.isdigit()) == 25,  # Regra 5: Soma dos dígitos
    lambda x: any(r in x for r in ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]),
    # Regra 6: Número romano
    lambda x: all(d in x for d in str(numero_sorteado)),  # Regra 7: Número sorteado
    lambda x: any(district in x for district in distritos),  # Regra 8: Distrito de Night City
    lambda x: "⭐⭐⭐⭐⭐" in x,  # Regra 9: Vitorias do brasil
    lambda s: (n := next((c for c in s if c.isdigit()), None)) and int(n) > 3 and int(n) % 2 == 0
    # Regra 10: Primeiro número par e maior que 3

]

# Definir mensagens de erro personalizadas para cada regra
mensagens_de_erro = [
    "A senha precisa ter pelo menos 5 caracteres",
    "A senha precisa ter pelo menos uma letra maiúscula",
    "A senha precisa ter pelo menos um número",
    "A senha precisa ter pelo menos um caractere especial",
    "A soma dos dígitos da senha precisa ser igual a 25",
    "A senha precisa conter um número romano entre I e X",
    f"A senha precisa conter o número {numero_sorteado}.",
    "A senha precisa conter o nome de um dos distritos de Night City (Cyberpunk 2077).",
    "A senha precisa conter a representação das vitórias do Brasil",
    '"O primeiro número da senha precisa ser par e maior que 3"'
]

# Validar a senha inserida pelo usuário
senha_valida = False
while not senha_valida:
    senha = input("Digite uma senha: ")

    for i, regra in enumerate(regras):
        if not regra(senha):
            print(mensagens_de_erro[i])
            break

    else:
        senha_valida = True

# Exibir a mensagem de validação de senha e o número sorteado se todas as regras forem satisfeitas
print(f"Senha válida!")
