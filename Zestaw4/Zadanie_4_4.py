# Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.

def fibonacci(number):
    if number == 0 or number == 1:
        return number

    previous_number = 0
    next_number = 1

    for i in range(number - 1):
        number_tmp = next_number
        next_number = previous_number + next_number
        previous_number = number_tmp

    return next_number


def main():
    n = input("Write number to calculate Fibonacci of it: ")

    print(fibonacci(n))


if __name__ == '__main__':
    main()
