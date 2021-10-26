# Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M) 
# na liczby arabskie (podać kilka sposobów tworzenia takiego słownika).

dictionary = {
    1:      "I",
    5:      "V",
    10:     "X",
    50:     "L",
    100:    "C",
    500:    "D",
    1000:   "M",
}

def printNumberInArabic(number_rom: str):
    result = 0
    previousPosition = 0

    for i in range(len(number_rom) - 1, -1, -1):
        for j in range(len(dictionary) - 1, -1, -1):
            r = str( list(dictionary.values())[j] )
            if number_rom[i] == r:
                if j >= previousPosition:
                    result += list(dictionary.keys())[list(dictionary.values()).index(number_rom[i])]
                    previousPosition = j
                else:
                    result -= list(dictionary.keys())[list(dictionary.values()).index(number_rom[i])]
                break

    print(number_rom + ' = ' + str(result))
                                

def main():
    user_input = input("Write number: ")
    printNumberInArabic(user_input) 
        

if __name__ == '__main__':
    main()