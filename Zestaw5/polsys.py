# Stworzyć plik polys.py i zapisać w nim funkcje do działań na wielomianach.

def add_poly(poly1, poly2):
    lengthFirst = len(poly1)
    lengthSecond = len(poly2)
    if lengthFirst >= lengthSecond:
        for i in range(lengthSecond):
            poly1[i] += poly2[i]
        return poly1
    elif lengthFirst < lengthSecond:
        for i in range(lengthFirst):
            poly2[i] += poly1[i]
        return poly2


def sub_poly(poly1, poly2):       # poly1(x) - poly2(x)
    lengthFirst = len(poly1)
    lengthSecond = len(poly2)
    if lengthFirst >= lengthSecond:
        for i in range(lengthSecond):
            poly1[i] -= poly2[i]
        return poly1
    elif lengthFirst < lengthSecond:
        for i in range(lengthFirst):
            poly2[i] -= poly1[i]
        return poly2


def mul_poly(poly1, poly2):       # poly1(x) * poly2(x)
    if len(poly1) < 1 or len(poly2) < 1:
        return 0
    res = list()
    for i in range((len(poly1) - 1) + (len(poly2) - 1) + 1):
        res.append(0)
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            res[i+j] += poly1[i] * poly2[j]
    return res


def mul(poly, n):
    for i in range(len(poly)):
        poly[i] *= n
    return poly


def is_zero(poly):             # bool, [0], [0,0], itp.
    for i in range(len(poly)):
        if poly[i] != 0:
            return False
    return True


def eq_poly(poly1, poly2):        # bool, porównywanie poly1(x) == poly2(x)
    if len(poly1) == len(poly2):
        for i in range(poly1):
            if poly1[i] != poly2:
                return False
        return True
    return False


def eval_poly(poly, x0):         # poly(x0), algorytm Hornera
    result = 0
    for i in range(len(poly) - 1, -1, -1):
        result = poly[i] + (x0 * result)
    return result


def combine_poly(poly1, poly2):     # poly1(poly2(x)), trudne!
    res = list()
    for i in range(len(poly1)):
        if i == 0:
            res.append(poly1[0])

        else:
            wsp = pow_poly(poly2, i)
            mul(wsp, poly1[i])
            res.append(wsp)
    if isinstance(res[-1], list):
        res2 = res[-1]
    else:
        res2 = [0]

    for i in range(1, len(res) - 1):
        res2 = add_poly(res2, res[i])
    res2[0] += res[0]

    return res2


def pow_poly(poly, n):            # poly(x) ** n
    if n == 1:
        return poly
    return (mul_poly(poly, pow_poly(poly, n - 1)))


def diff_poly(poly):
    if len(poly) - 1 != 0:
        for i in range(len(poly) - 1):
            poly[i] = (i + 1) * poly[i + 1]
            poly[i + 1] = 0

        return poly
    return poly

l1 = [0, 0, 2, 3]
l2 = [1, 2]

print(combine_poly(l2, l1))