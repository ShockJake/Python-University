# Podać sposób wyświetlania napisu word tak, aby jego znaki były rozdzielone znakiem podkreślenia.

def main():
    underline("word")


def underline(s):
    print('_'.join(s))


if __name__ == "__main__":
    main()
