# Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line. 
# Zbudować napis stworzony z ostatnich znaków wyrazów z wiersza line.


def func():
    line = "There are some words"

    first_chars = ""

    last_chars = ""

    print('Line: ' + line)
    line = line.split()

    for i in line:
        word = i
        first_chars += word[0]
        last_chars += word[len(word)-1]

    # for i in line:
    #     first_chars.join(i[0])
    #     n = len(i)
    #     last_chars.join(i[n-1])
    print('First characters: ' + first_chars)
    print('Last characters: ' + last_chars)

def main():
    func()

if __name__ == "__main__":
    main()