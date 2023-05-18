retorno = ["sena", "quina", "quadra", "terno", "azar", "azar", "azar"]

AP = [int(x) for x in input().split(' ')]
RESULT = [int(x) for x in input().split(' ')]

AP = set(AP)

for dezena in RESULT:
    if dezena in RESULT:
        AP.remove(dezena)

print(retorno[len(AP)])
