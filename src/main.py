import os
import random

print("IMPORTANT! \n Make sure you're running this file from outside of the 'src' directory.\n\n")

dirs = os.listdir("docs/")

print("Welcome to Pictionary!")

print("What file do you want to use? (ex. test.txt)")
print("\tFiles Available for Use:")
for file in dirs:
    print("\t\t" + file)

fileName = input()

file = open("docs/" + fileName)
wordList = []
numList = []
go = True

for words in file:
    wordList.append(words)
file.close()

totalLength = len(wordList)
print("There are " + str(totalLength) + " total words in this file.")

while go:
    num = random.randint(0, len(wordList) - 1)
    if num not in numList:
        answer = input("\n Want to Play? Y/N ").lower()
        if answer == "y":
            go = True

            numList.append(num)
            word = wordList[num].strip()
            print(word)

            numLength = len(numList)
            print("You have played " + str(numLength) + " words out of " + str(totalLength))

        else:
            go = False

    else:
        if numLength != totalLength:
            continue

        else:
            go = False

print("Thanks for playing!")

