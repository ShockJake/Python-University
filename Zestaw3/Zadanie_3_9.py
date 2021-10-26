# Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby. 
# Znaleźć listę zawierającą sumy liczb z tych sekwencji.

def sumOfSequence():
    nums = [[], [4], (1,2), [3, 4], (5, 6, 7)]

    summed_nums = []

    for i in range(len(nums)):
        summed_nums.append(sum(nums[i]))

    print(summed_nums)


def main():
    sumOfSequence()

if __name__ == "__main__":
    main()
