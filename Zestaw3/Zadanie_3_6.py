# Napisać program rysujący prostokąt zbudowany z małych kratek. 
# Należy zbudować pełny string, a potem go wypisać.

def draw():
    x = input('Write width of rectangle: ')
    y = input('Write higth of rectanlge: ')

    str1 = '+---'
    str1_end = '+\n'
    str2 = '|   '
    str2_end = '|\n'
    result = ''
    
    for i in range(int(y)):
        for i in range(int(x)):
            result += str1
        result += str1_end
        for i in range(int(x)):
            result += str2
        result += str2_end
    for i in range(int(x)):
        result += str1
    result += str1_end
    
    print(result)

def main():
    draw()

if __name__ == "__main__":
    main()