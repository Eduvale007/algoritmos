# Algoritmo de Ordenação por Seleção em Python

Este repositório contém uma implementação simples do algoritmo de **ordenação por seleção** (*Selection Sort*) em Python, com o objetivo de fins educacionais.

---

## 📌 O que é Ordenação por Seleção?

A ordenação por seleção é um algoritmo de ordenação simples que funciona da seguinte forma:

1. Procura o menor elemento da lista.
2. Remove esse elemento da lista original.
3. Adiciona esse elemento em uma nova lista.
4. Repete o processo até que a lista original esteja vazia.

---

## 🧠 Como o código funciona

### 1. `buscaMenor(arr)`

Essa função percorre a lista e retorna o **índice** do menor valor encontrado.

🚀 Observações
Este algoritmo não é eficiente para listas grandes (complexidade O(n²)).

Foi implementado com foco didático, para mostrar o funcionamento interno da ordenação.

Para aplicações reais, o ideal é usar sorted(lista) ou lista.sort() que são muito mais otimizados.

```python
def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice


def ordenacaoporSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr