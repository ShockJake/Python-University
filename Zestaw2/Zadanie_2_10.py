# Mamy dany napis wielowierszowy line.
# Podać sposób obliczenia liczby wyrazów w napisie.
# Przez wyraz rozumiemy ciąg "czarnych" znaków, oddzielony od innych wyrazów białymi znakami (spacja, tabulacja, newline).


def func():
    line = "a\nb c\n\nd \t e"

    print(line)

    print(line.__len__())

def main():
    func()

if __name__ == "__main__":
    main()