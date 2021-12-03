# Obliczyć liczbę pi za pomocą algorytmu Monte Carlo.
# Wykorzystać losowanie punktów z kwadratu z wpisanym kołem.
# Sprawdzić zależność dokładności wyniku od liczby losowań.

import random


def calc_pi(n=100):
    circle_radius = 1
    points_inside_circle = 0
    points_inside_square = 0
    pi = 0.0
    pi_result = 0.0
    for i in range(n):
        x = random.randint(0, 1000)/1000
        y = random.randint(0, 1000)/1000
        if x*x+y*y <= circle_radius:
            points_inside_circle += 1
        points_inside_square += 1
        pi = 4 * points_inside_circle/points_inside_square
        if(round(pi, 2) == 3.14):
            pi_result = pi

        print('Pi = ' + str(pi))

    return pi_result


def main():
    print(calc_pi(1000))


if __name__ == '__main__':
    main()
