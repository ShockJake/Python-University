# Dla dwóch sekwencji liczb lub znaków znaleźć: 
# (a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń), 
# (b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).

def commonElements():
    sequence_1 = '13578'
    sequence_2 = '24678'
    commonElements = []
    all_elements = []
    
    for i in range(len(sequence_1)):
        if sequence_1[i] not in all_elements:
            all_elements.append(sequence_1[i])
        if sequence_2.find(sequence_1[i]) != -1:
            if (sequence_1[i]) not in commonElements:
                commonElements.append(sequence_1[i])

    for i in range(len(sequence_2)):
        if sequence_2[i] not in all_elements:
            all_elements.append(sequence_2[i])            
        
    print('Common elements: ' + str(commonElements))
    print('All elements: ' + str(all_elements))


def main():
    commonElements()

if __name__ == '__main__':
    main()