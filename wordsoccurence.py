s = "Hallo dit is een stukje tekst, met een paar woorden die die herhaalt herhaalt worden worden."

text = s.lower().replace(',', '').replace('.', '')

list_of_words = text.split()

set_of_words = set(list_of_words)

d = {} # d = dict()
for word in set_of_words:
    count = text.count(word)
    d[word] = count 

for w,c in d.items(): # [(word1, count1), (word2, count2), ...]
    print(f"The word '{w}' occurs {c} times")