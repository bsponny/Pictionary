import random

file = open("Pictures")
wordList = []

for words in file:
    wordList.append(words)

num = random.randint(0, len(wordList))
print(wordList[num])
file.close()