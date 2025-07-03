

def pesquisa_binaria(lista, alvo):
    inicio, fim = 0, len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio -1
        
    
    return -1

lista = [8, 14, 25, 40, 56, 62, 71]

print(pesquisa_binaria(lista,56))
