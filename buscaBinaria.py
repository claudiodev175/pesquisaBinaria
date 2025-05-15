# Lista de números já ordenada
lista = [1, 3, 5, 7, 9, 11, 13]

# Valor que queremos buscar na lista
alvo = 7

# Índice inicial da busca
inicio = 0

# Índice final da busca
fim = len(lista) - 1

# Variável para armazenar o índice do elemento encontrado
encontrado = -1

# Loop que continua enquanto ainda há elementos para buscar
while inicio <= fim:
    # Calcula o índice do meio da lista
    meio = (inicio + fim) // 2

    # Verifica se o valor do meio é igual ao alvo
    if lista[meio] == alvo:
        encontrado = meio  # Armazena o índice encontrado
        break  # Encerra o loop
    # Se o valor do meio for menor que o alvo, busca na metade direita
    elif lista[meio] < alvo:
        inicio = meio + 1
    # Caso contrário, busca na metade esquerda
    else:
        fim = meio - 1

# Após sair do loop, verifica se encontrou o valor
if encontrado != -1:
    print(f"Elemento encontrado no índice {encontrado}")
else:
    print("Elemento não encontrado")
