# Napisać program rysujący "miarkę" o zadanej długości. 
# Należy prawidłowo obsłużyć liczby składające się z kilku cyfr (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej). 
# Należy zbudować pełny string, a potem go wypisać.

def draw():
    size = int(input("Write size of a scale: "))

    char1 = '|....'
    char2 = '|\n'
    result = ''
    for i in range(size):
        result += char1
    result += char2
    for i in range(size + 1):
        result += str(i)
        result += '    '
    print(result)


def main():
    draw()

if __name__ == "__main__":
    main()