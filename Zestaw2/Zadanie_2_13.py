# Znaleźć łączną długość wyrazów w napisie line.

def main():
    sumOf("I'm a new student")


def sumOf(s):
    sum = 0
    words = str(s).split(' ')
    for word in words:
        sum += len(word)
    print(sum)    


if __name__ == "__main__":
    main()
