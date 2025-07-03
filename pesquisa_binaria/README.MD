# 🔍 Pesquisa Binária em Python

A **pesquisa binária** (ou **busca binária**) é um algoritmo eficiente para encontrar um elemento em uma **lista ordenada**. Ele funciona dividindo a lista pela metade repetidamente até encontrar o elemento desejado — ou concluir que ele não está presente.

---

## 🧠 Como a pesquisa binária funciona?

Imagine que você está procurando por uma palavra em um dicionário. Em vez de ler página por página, você abre o meio do livro e decide se deve procurar na metade da frente ou de trás. É isso que a busca binária faz!

### Etapas:

1. Começa olhando o elemento do **meio da lista**.
2. Se for o elemento que você quer → retorna a posição.
3. Se o elemento for **menor**, busca na **metade direita**.
4. Se for **maior**, busca na **metade esquerda**.
5. Repete o processo até encontrar ou acabar a lista.

> 🟡 Importante: a lista precisa estar **ordenada** para que a busca binária funcione corretamente!

---



🧹 Complexidade
Melhor caso: O elemento está no meio → O(1)

Pior caso: Precisa dividir várias vezes → O(log n)

Ou seja, a busca binária é muito mais rápida que uma busca simples (O(n)) quando a lista é grande.

✅ Vantagens:
Muito eficiente em listas grandes.

Fácil de implementar.

Evita percorrer todos os elementos.

⚠️ Limitações:
Só funciona em listas ordenadas.

Requer acesso direto aos elementos da lista (como em arrays ou listas Python).

📌 Dica extra:
Se a lista não estiver ordenada, você pode ordená-la primeiro com:


lista.sort()



## 🧾 Código Python

```python
def pesquisa_binaria(lista, alvo):
    inicio, fim = 0, len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
        
    return -1


 