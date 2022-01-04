# Przygotować moduł Pythona z funkcjami tworzącymi listy liczb całkowitych do sortowania. Przydatne są m.in. następujące rodzaje danych:
# (a) różne liczby int od 0 do n-1 w kolejności losowej,
# (b) różne liczby int od 0 do n-1 prawie posortowane (liczby są blisko swojej prawidłowej pozycji),
# (c) różne liczby int od 0 do n-1 prawie posortowane w odwrotnej kolejności,
# (d) n liczb float w kolejności losowej o rozkładzie gaussowskim,
# (e) n liczb int w kolejności losowej, o wartościach powtarzających się, należących do zbioru k elementowego (k < n, np. k^2 = n).

import random
import math
from typing import List


def randomIntegerNumbers(number):  # podpunkt a
    List = []
    for i in range(number):
        List.append(i)
    random.shuffle(List)
    return List


def almostSortedIntegerNumbers(number):  # podpuntk b
    List = []
    for i in range(number):
        List.append(i)
    for i in range(0, number, 2):
        if i < number - 1:
            element = List[i]
            List[i] = List[i+1]
            List[i+1] = element
    return List


def almostSortedIntNumsReversed(number):  # podpunkt c
    List = almostSortedIntegerNumbers(number)
    List.reverse()
    return List


def randomFloatNumbersInGaussian(number):  # podpunkt d
    s = 7
    a = 14
    List = []
    for i in range(number):
        List.append(random.gauss(a, s))
    return List

def randomIntOfK(number): # podpunkt e
    List = []
    k = math.sqrt(number)
    k = math.ceil(k)
    
    for i in range(number):
        List.append(random.randint(0, k))
    return List