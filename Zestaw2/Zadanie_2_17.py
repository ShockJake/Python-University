# Posortować wyrazy z napisu line raz alfabetycznie, a raz pod względem długości.

from enum import Enum

class Sort(Enum):
    BY_ALPHABET = 0
    BY_LENGTH = 1

def main():

    str = 'Stanly Chris Jane Ray'

    sort(str, Sort.BY_LENGTH)


def sort(s: str, sort_by: Sort):
    words = s.split(' ')
    if sort_by == Sort.BY_ALPHABET:
        print(sorted(words))
    elif sort_by == Sort.BY_LENGTH:
        print(sorted(words, key=len))


if __name__ == "__main__":
    main()
