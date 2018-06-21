from collections import Counter
import sys

key = sys.argv.pop(1)
sen = ""

while(1):
    i = input()
    sen += i
    if i == "":
        break

dic = str.maketrans("-", " ", ",.;—!'")
sen = sen.translate(dic)

sen = list(sen.split())

counter = Counter(sen)

frec = { word:cnt for word, cnt in counter.most_common()}

print(key + ":" + str(frec[key]))