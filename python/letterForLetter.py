import random

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
word1 =list(word1)
word2 = list(word2)

for i in range(len(word1)):
    x = random.randrange(0, len(word1))
    if word1[i] == word2[i]:
        continue
    else:
        word1[i] = word2[i]
        print(''.join(word1))
