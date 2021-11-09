# Wielomian będzie reprezentowany przez listę swoich współczynników, np. [a0, a1, a2] dla a0 + a1*x + a2*x*x. Napisać kod testujący moduł polys.

import unittest
from polsys import*


class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [0, 1]      # W(x) = x
        self.p2 = [0, 0, 1]   # W(x) = x*x

    def test_add_poly(self):
        print('add')
        self.assertEqual(add_poly(self.p1, self.p2), [0, 1, 1])

    def test_sub_poly(self):
        print('sub')
        self.assertEqual(sub_poly(self.p1, self.p2), [0, -1, 1])

    def test_mul_poly(self):
        print('mul')
        self.assertEqual(mul_poly(self.p1, self.p2), [0, 0, 0, 1])

    def test_is_zero(self):
        print('is_zero')
        self.assertEqual(is_zero(self.p1), False)

    def test_cmp_poly(self):
        print('compare')
        self.assertEqual(eq_poly(self.p1, self.p2), False)

    def test_eval_poly(self):
        print('eval')
        self.assertEqual(eval_poly(self.p2, 2), 4)
        print(eval_poly(self.p2, 2))

    def test_combine_poly(self):
        print('combine')
        self.assertEqual(combine_poly(self.p1, self.p2), [0, 0, 1])

    def test_pow_poly(self):
        print('pow')
        self.assertEqual(pow_poly(self.p2, 3), [0, 0, 0, 0, 0, 0, 1])

    def test_diff_poly(self):
        print('diff')
        self.assertEqual(diff_poly(self.p2), [0, 2, 0])

    def tearDown(self):
        print('Ok')


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
