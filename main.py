import random

file = open("ChristmasPictures")
wordList = []

for words in file:
    wordList.append(words)

num = random.randint(0, len(wordList))
print(wordList[num])
file.close()