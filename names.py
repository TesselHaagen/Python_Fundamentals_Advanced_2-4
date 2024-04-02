names = []

while True:
    name = input("Please provide a name: ")
    if name == '':
        break

    names.append(name)


while True:
    name = input("Please provide a name: ")
    if name: 
        names.append(name)
    else:
        break

while True:
    name = input("Please provide a name: ")
    if not name: 
        break
    names.append(name)

names.sort()
names_sorted = sorted(names)

for name in names:
    print(name)