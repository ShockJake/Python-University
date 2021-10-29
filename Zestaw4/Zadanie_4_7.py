# Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami,
# a takie zagnieżdżenia mogą się nakładać do nieograniczonej głębokości.
# Napisać funkcję flatten(sequence), która zwróci spłaszczoną listę wszystkich elementów sekwencji.

def flatten(sequence, result):
    for i in sequence:
        if(isinstance(i, int)):
            result.append(i)
        else:
            flatten(i, result)
    return result


def main():
    sequence = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
    result = []
    print(flatten(sequence, result))


if __name__ == "__main__":
    main()
