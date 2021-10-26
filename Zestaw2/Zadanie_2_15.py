# Na liście L znajdują się liczby całkowite dodatnie. 
# Stworzyć napis będący ciągiem cyfr kolejnych liczb z listy L.

def main():

    ints = [15, 18, 4, 93, 57]
    
    stringOf(ints)


def stringOf(ints):
    res = ''
    for int in ints:
        res += str(int)
    print(res)       


if __name__ == "__main__":
    main()
