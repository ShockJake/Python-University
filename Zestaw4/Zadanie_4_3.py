# Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.

def factorial(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res


def main():
    n = input("Write number to calculate factorial of it: ")
    print(factorial(int(n)))


if __name__ == '__main__':
    main()
