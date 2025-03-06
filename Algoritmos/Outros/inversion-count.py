# Algoritmo de contagem de inversões
# Objetivo: Contar quantos pares de elementos estão "invertidos"
#           em relação à ordem crescente no array.
#
# O algoritmo verifica todos os pares (i, j) onde i < j e arr[i] > arr[j].
# Caso a condição seja satisfeita, significa que esses elementos estão "fora de ordem"
# e são considerados como uma inversão.
#
# Complexidade: O(n²), pois o algoritmo utiliza dois loops aninhados para comparar todos os pares.


def inversionCount(arr):
    n = len(arr)
    invCount = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                invCount += 1
    return invCount


print(inversionCount([1, 3, 2]))  # Resultado: 1
print(inversionCount([4, 3, 2, 1]))  # Resultado: 6
print(inversionCount([2, 1]))  # Resultado: 1
