import random

file = open("ChristmasPictures")
wordList = []
numList = []
go = True

for words in file:
    wordList.append(words)

while go:
    answer = input("Keep going? Y/N ").lower()

    if answer == "y":
        go = True
    else:
        go = False
        break
    
    num = random.randint(0, len(wordList))
    
    if num in numList and answer != "y":
        continue
    else:
        numList.append(num)
        print(wordList[num])

print("Thanks for playing!")

file.close()
