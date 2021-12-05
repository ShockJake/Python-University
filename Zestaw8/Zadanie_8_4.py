# Zaimplementować algorytm obliczający pole powierzchni trójkąta,
# jeżeli dane są trzy liczby będące długościami jego boków.
# Jeżeli podane liczby nie spełniają warunku trójkąta, to program ma generować wyjątek ValueError.

from math import sqrt


def heron(a, b, c):
    if a == 0 or b == 0 or c == 0:
        raise ValueError()
    if ((a + b) < c) or ((a + c) < b) or ((b + c) < a):
        raise ValueError()
    p = (a + b + c) / 2
    return round(sqrt((p * (p - a) * (p - b) * (p - c))), 4)


def main():
    while True:
        try:
            a = int(input('Write first side of triangle: '))
            b = int(input('Write second side of triangle: '))
            c = int(input('Write third sied of triangle: '))
            print(heron(a, b, c))
        except ValueError:
            print('Error - Given number are not satisfied with posible arguments')


if __name__ == '__main__':
    main()
