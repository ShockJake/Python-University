# -*- coding utf-8 -*-
# Zbadać problem szukania rozwiązań równania liniowego postaci a * x + b * y + c = 0.
# Podać specyfikację problemu. Podać algorytm rozwiązania w postaci listy kroków,
# schematu blokowego, drzewa. Podać implementację algorytmu w Pythonie w postaci funkcji solve1(),
# która rozwiązania wypisuje w formie komunikatów.

def solve1(a, b, c):
    if a == 0 and b != 0:
        y = -(c / b)
        print('Pierwiastkiem równania jest każda para liczb w postaci (r, ' +
              str(y) + '), gdize r wybieramy dowolnie.')
    if a != 0 and b == 0:
        x = -(c / a)
        print('Pierwiastkiem równania jest każda para liczb w postaci (' +
              str(x) + ', r), gdize r wybieramy dowolnie.')
    if a != 0 and b != 0:
        y1 = -(a / b)
        y2 = -(c / b)
        y = str(y1) + ' * r - ' + str(y2)
        print('Pierwiastkiem równania jest każda para liczb w postaci (r, ' +
              y + '), gdize r wybieramy dowolnie.')


def main():
    solve1(2, 3, 4)


if __name__ == '__main__':
    main()
