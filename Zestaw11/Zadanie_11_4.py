# Porównaj czasy działania wybranych algorytmów dla listy zawierającej n różnych liczb, przy n = 10^2, 10^3, 10^4, 10^5, 10^6.

import Zadanie_11_1 as numGen
import datetime as dt

# --- Algorithms ---


def mergesort(L, left, right):
    """Sortowanie przez scalanie."""
    if left < right:
        middle = (left + right) // 2   # wyznaczanie środka
        mergesort(L, left, middle)
        mergesort(L, middle + 1, right)
        merge(L, left, middle, right)   # scalanie


def merge(L, left, middle, right):
    """Łączenie posortowanych sekwencji."""
    T = [None] * (right - left + 1)
    left1 = left
    right1 = middle
    left2 = middle + 1
    right2 = right
    i = 0
    while left1 <= right1 and left2 <= right2:
        if L[left1] <= L[left2]:   # mniejsze lub równe
            T[i] = L[left1]
            left1 += 1
        else:
            T[i] = L[left2]
            left2 += 1
        i += 1
    # Lewa lub prawa część może mieć elementy.
    while left1 <= right1:
        T[i] = L[left1]
        left1 += 1
        i += 1
    while left2 <= right2:
        T[i] = L[left2]
        left2 += 1
        i += 1
    # Skopiuj z tablicy tymczasowej do oryginalnej.
    for i in range(right - left + 1):
        L[left + i] = T[i]


def insertsort(L, left, right):
    for i in range(left+1, right+1):   # L[left] jest posortowany
        item = L[i]
        j = i
        while j > left and L[j-1] > item:
            L[j] = L[j-1]   # robimy miejsce na item
            j = j-1
        L[j] = item


def bubblesort(L, left, right):
    limit = right
    while True:
        k = left-1   # lewy wskaźnik przestawianej pary
        for i in range(left, limit):
            if L[i] > L[i+1]:
                temp = L[i+1]
                L[i+1] = L[1]
                L[i] = temp
                k = i
        if k > left:
            limit = k
        else:
            break


def quicksort(L, left, right):
    """Sortowanie szybkie wg Cormena str. 169."""
    if left >= right:
        return
    pivot = partition(L, left, right)
    # pivot jest na swoim miejscu.
    quicksort(L, left, pivot - 1)
    quicksort(L, pivot + 1, right)


def partition(L, left, right):
    """Zwraca indeks elementu rozdzielającego."""
    # Element rozdzielający to ostatni z prawej,
    # dlatego na końcu trzeba go przerzucić do środka.
    # Będzie on na docelowej pozycji ze względu na sortowanie.
    x = L[right]   # element rozdzielający
    i = left
    for j in range(left, right):
        if L[j] <= x:
            temp = L[i]
            L[i] = L[j]
            L[j] = temp
            i += 1
    temp = L[i]
    L[i] = L[right]
    L[right] = temp
    return i

# --- Algorithms ---

# --- Tests ---


def testN2():
    N = 10**2
    List = numGen.randomIntegerNumbers(N)

    List2 = List.copy()
    beginingTime = dt.datetime.now()
    mergesort(List2, 0, N - 1)
    endingTime = dt.datetime.now()
    duration = endingTime - beginingTime
    print('N^2 mergesort -> ' + str(duration))

    List2 = List.copy()
    beginingTime = dt.datetime.now()
    insertsort(List2, 0, N - 1)
    endingTime = dt.datetime.now()
    duration = endingTime - beginingTime
    print('N^2 insertsort -> ' + str(duration))

    List2 = List.copy()
    beginingTime = dt.datetime.now()
    bubblesort(List2, 0, N - 1)
    endingTime = dt.datetime.now()
    duration = endingTime - beginingTime
    print('N^2 bubblesort -> ' + str(duration))

    List2 = List.copy()
    beginingTime = dt.datetime.now()
    quicksort(List2, 0, N - 1)
    endingTime = dt.datetime.now()
    duration = endingTime - beginingTime
    print('N^2 quicksort -> ' + str(duration))


def testN3():
    N = 10**3
    List = numGen.randomIntegerNumbers(N)

    List2 = List.copy()
    beginingTime = dt.datetime.now()
    mergesort(List2, 0, N - 1)
    endingTime = dt.datetime.now()
    duration = endingTime - beginingTime
    print('N^3 - mergesort -> ' + str(duration))

    List2 = List.copy()
    beginingTime = dt.datetime.now()
    insertsort(List2, 0, N - 1)
    endingTime = dt.datetime.now()
    duration = endingTime - beginingTime
    print('N^3 insertsort -> ' + str(duration))

    List2 = List.copy()
    beginingTime = dt.datetime.now()
    bubblesort(List2, 0, N - 1)
    endingTime = dt.datetime.now()
    duration = endingTime - beginingTime
    print('N^3 bubblesort -> ' + str(duration))

    List2 = List.copy()
    beginingTime = dt.datetime.now()
    quicksort(List2, 0, N - 1)
    endingTime = dt.datetime.now()
    duration = endingTime - beginingTime
    print('N^3 quicksort -> ' + str(duration))


def testN4():
    N = 10**4
    List = numGen.randomIntegerNumbers(N)

    List2 = List.copy()
    beginingTime = dt.datetime.now()
    mergesort(List2, 0, N - 1)
    endingTime = dt.datetime.now()
    duration = endingTime - beginingTime
    print('N^4 - mergesort -> ' + str(duration))

    List2 = List.copy()
    beginingTime = dt.datetime.now()
    insertsort(List2, 0, N - 1)
    endingTime = dt.datetime.now()
    duration = endingTime - beginingTime
    print('N^4 insertsort -> ' + str(duration))

    List2 = List.copy()
    beginingTime = dt.datetime.now()
    bubblesort(List2, 0, N - 1)
    endingTime = dt.datetime.now()
    duration = endingTime - beginingTime
    print('N^4 bubblesort -> ' + str(duration))

    # List2 = List.copy()
    # beginingTime = dt.datetime.now()
    # quicksort(List2, 0, N - 1) Interpretator zgłasza przepełnienie głenbokoszci rekurencji
    # endingTime = dt.datetime.now()
    # duration = endingTime - beginingTime
    # print('N^4 quicksort -> ' + str(duration))


def testN5():
    N = 10**5
    List = numGen.randomIntegerNumbers(N)

    List2 = List.copy()
    beginingTime = dt.datetime.now()
    mergesort(List2, 0, N - 1)
    endingTime = dt.datetime.now()
    duration = endingTime - beginingTime
    print('N^5 - mergesort -> ' + str(duration))

    List2 = List.copy()
    beginingTime = dt.datetime.now()
    insertsort(List2, 0, N - 1)
    endingTime = dt.datetime.now()
    duration = endingTime - beginingTime
    print('N^5 insertsort -> ' + str(duration))

    List2 = List.copy()
    beginingTime = dt.datetime.now()
    bubblesort(List2, 0, N - 1)
    endingTime = dt.datetime.now()
    duration = endingTime - beginingTime
    print('N^5 bubblesort -> ' + str(duration))

    # List2 = List.copy()
    # beginingTime = dt.datetime.now()
    # quicksort(List2, 0, N - 1) Interpretator zgłasza przepełnienie głenbokoszci rekurencji
    # endingTime = dt.datetime.now()
    # duration = endingTime - beginingTime
    # print('N^5 quicksort -> ' + str(duration))


def testN6():
    N = 10**6
    List = numGen.randomIntegerNumbers(N)

    List2 = List.copy()
    beginingTime = dt.datetime.now()
    mergesort(List2, 0, N - 1)
    endingTime = dt.datetime.now()
    duration = endingTime - beginingTime
    print('N^6 - mergesort -> ' + str(duration))

    List2 = List.copy()
    beginingTime = dt.datetime.now()
    insertsort(List2, 0, N - 1)
    endingTime = dt.datetime.now()
    duration = endingTime - beginingTime
    print('N^6 insertsort -> ' + str(duration))

    List2 = List.copy()
    beginingTime = dt.datetime.now()
    bubblesort(List2, 0, N - 1)
    endingTime = dt.datetime.now()
    duration = endingTime - beginingTime
    print('N^6 bubblesort -> ' + str(duration))

    # List2 = List.copy()
    # beginingTime = dt.datetime.now()
    # quicksort(List2, 0, N - 1) Interpretator zgłasza przepełnienie głenbokoszci rekurencji
    # endingTime = dt.datetime.now()
    # duration = endingTime - beginingTime
    # print('N^6 quicksort -> ' + str(duration))


def testAll():
    testN2()
    print()
    print()

    testN3()
    print()
    print()

    testN4()
    print()
    print()

    testN5()
    print()
    print()

    testN6()

# --- Tests ---


def main():
    print('Test')
    testAll()


if __name__ == '__main__':
    main()
