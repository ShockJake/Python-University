# Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie.
# Chcemy zbudować napis z trzycyfrowych bloków, gdzie liczby jedno- i dwucyfrowe będą miały blok dopełniony zerami, np. 007, 024.

def func():
    list_int = [1, 22, 333]
    list_str = ""

    for i in list_int:
        list_str += str(i) + " "

    list_str = list_str.split()

    for i in range(len(list_str)):
        list_str[i] = list_str[i].zfill(3)
    print(list_str)


def main():
    func()

if __name__ == "__main__":
    main()