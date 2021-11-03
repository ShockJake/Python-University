# Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w napisie line.

def findLongestWord(string):
    print("Line: " + string)

    line = string.split()

    word = max(line)

    print("The biggest word: " + word)
    print("Length of the biggest word: " + str(len(word))) 

def main():
    line = "There are some worlds"
    findLongestWord(line)

if __name__ == "__main__":
    main()