# Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji,
# które zwracają pełny string przez return.
# Funkcje nie powinny pytać użytkownika o dane, tylko korzystać z argumentów.

def make_ruler(n):

    size = n

    char1 = '|....'
    char2 = '|\n'
    result = ''
    for i in range(size):
        result += char1
    result += char2
    for i in range(size + 1):
        result += str(i)
        result += '    '
    print(result)


def make_grid(rows, cols):

    x = rows
    y = cols

    str1 = '+---'
    str1_end = '+\n'
    str2 = '|   '
    str2_end = '|\n'
    result = ''

    for i in range(int(y)):
        for i in range(int(x)):
            result += str1
        result += str1_end
        for i in range(int(x)):
            result += str2
        result += str2_end
    for i in range(int(x)):
        result += str1
    result += str1_end

    print(result)


def main():
    n = int(input("Write size of a scale: "))
    make_ruler(n)

    rows = input('Write width of rectangle: ')
    cols = input('Write higth of rectanlge: ')

    make_grid(rows, cols)


if __name__ == "__main__":
    main()
