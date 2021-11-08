# Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, 
# która może zawierać zagnieżdżone podsekwencje. Wskazówka: rozważyć wersję rekurencyjną,
# a sprawdzanie, czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).

def sum_seq(sequence, result):
    for i in sequence:
        if isinstance(i, int):
            result += i
        else:
            result = sum_seq(i, result)

    return result


def main():
    sequence = [1, 2, 3, [1, 1], [2, [4, 7]]]
    result = 0
    print(sum_seq(sequence, result))


if __name__ == '__main__':
    main()
