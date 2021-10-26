# Znaleźć liczbę cyfr zero w dużej liczbie całkowitej.

def func():
    number = 1000100101001

    number_str = str(number)

    print(number_str.count('0'))

def main():
    func()

if __name__ == "__main__":
    main()
