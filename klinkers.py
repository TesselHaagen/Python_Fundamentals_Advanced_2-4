tekst = input("Geef een tekst:")

vowels = ['a', 'o', 'e', 'i', 'u', 'y']

total_count = 0
for v in vowels:
    count = tekst.count(v)
    total_count = total_count + count # total_count += count
    print(f"De klinker {v} komt {count} keer voor")

print(f"Er komen in totaal {total_count} klinkers voor in de tekst")