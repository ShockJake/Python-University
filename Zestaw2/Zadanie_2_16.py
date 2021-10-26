# W tekście znajdującym się w zmiennej line zamienić ciąg znaków "GvR" na "Guido van Rossum".

def func(str1, str2):
    line1 = str(str1)
    line2 = str(str2)

    line1.split()
    line2.split()
    
    line1 = ''

    for i in line2:
        line1 += i

    print("Line 1 after changing: " + line1)

def main():
    line1 = "GvR"
    line2 = "Guido van Rossum"

    print("Line 1: " + line1)
    print("Line 2: " + line2)
    func(line1, line2)

if __name__ == "__main__":
    main()