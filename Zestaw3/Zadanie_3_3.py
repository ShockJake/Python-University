#Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3

def loop():
    for i in range(30):
        if i % 3 == 0:
            continue
        print(i)

def main():
    loop()

if __name__ == "__main__" :
    main()