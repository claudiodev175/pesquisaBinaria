# 🔍 Busca Binária em Python (Sem Funções)

## 📘 Disciplina

**Laboratório de Programação**

## 👨‍🏫 Professor

**Vinícius Amador**

## 👥 Grupo

- Cláudio Vinícius Coelho Barros  
- Matheus Machado  
- Julio César  
- Caio Henrique  

---

## 📚 Sobre o Algoritmo

A **Busca Binária** é um algoritmo eficiente para localizar um valor dentro de uma lista **ordenada**. A cada iteração, ela reduz o espaço de busca pela metade, até encontrar (ou não) o valor procurado.

### 🧠 Como funciona?

1. Define dois ponteiros: `início` e `fim`.
2. Enquanto `início <= fim`:
   - Calcula o índice `meio`.
   - Compara `lista[meio]` com o `alvo`.
   - Se igual, retorna o índice.
   - Se menor, ajusta `início`.
   - Se maior, ajusta `fim`.
3. Se não encontrar o elemento, retorna -1.

---

## 💻 Código (busca_binaria_simples.py)

```python
# Lista ordenada de elementos
lista = [1, 3, 5, 7, 9, 11, 13]

# Valor que queremos encontrar
alvo = 7

# Índices de controle
inicio = 0
fim = len(lista) - 1
encontrado = -1

# Algoritmo de busca binária
while inicio <= fim:
    meio = (inicio + fim) // 2

    if lista[meio] == alvo:
        encontrado = meio
        break
    elif lista[meio] < alvo:
        inicio = meio + 1
    else:
        fim = meio - 1

# Resultado
if encontrado != -1:
    print(f"Elemento encontrado no índice {encontrado}")
else:
    print("Elemento não encontrado")
