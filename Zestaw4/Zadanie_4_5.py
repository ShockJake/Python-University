# Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do right włącznie.
# Lista jest modyfikowana w miejscu (in place).
# Rozważyć wersję iteracyjną i rekurencyjną.

def iterateRevrse(L, left, right):

    if right < 1:
        return
    if left < 0:
        return
    if left > len(L) - 2:
        return
    if left >= right:
        return
    if right > len(L) - 1:
        return

    n = int((right+1 - left) // 2)

    for i in range(n):
        temp = L[left + i]
        L[left + i] = L[right - i]
        L[right - i] = temp


def recursiveRevesre(L, left, right):
    if right < 1:
        return
    if left < 0:
        return
    if left > len(L) - 2:
        return
    if left >= right:
        return
    if right > len(L) - 1:
        return

    L[left], L[right] = L[right], L[left]

    recursiveRevesre(L, left + 1, right - 1)


def main():
    L1 = [1, 2, 3, 4, 5, 6]
    iterateRevrse(L1, 2, 5)
    L2 = [1, 2, 3, 4, 5, 6]
    recursiveRevesre(L2, 0, 5)

    print('reversed iterally')
    print(L1)
    print('reversed recursively')
    print(L2)


if __name__ == '__main__':
    main()
