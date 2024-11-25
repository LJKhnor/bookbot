def countWords(text):
    words = text.split()
    return len(words)

def countCharacters(text):
    carList = {}
    alphabet = list(map(chr, range(97, 123)))
    for car in text:
        lower_car = car.lower()
        # print(lower_car)
        if lower_car in alphabet:
            if lower_car in list(carList):
                carList[lower_car] += 1
            else:
                carList[lower_car] = 1        
    return dict(sorted(carList.items(),key=lambda t: t[1], reverse=True))

def doReport(text):
    print('--- Begin report of books/frankenstein.txt ---')
    countWord = countWords(text)
    print(countWord, 'words found in the document')
    print()
    cCars = countCharacters(text)
    # print(cCars)
    for k,v in cCars.items():
        print('The ',k,' character was found ',v,' times')
    print('--- End report ---')

def main():
    with open('books/frankenstein.txt') as f:
        file_content = f.read()
        doReport(file_content)



if __name__ == "__main__":
    main()