def number_of_vowels(word: str):
    """
    Counts the number of vowels in a word

    Arguments:
    - word (str): the word to count the vowels in

    Returns:
     Integer: the number of vowels in a word
    """
    vowels = 'aeiuoy' # ['a', 'e', ....]

    count_v = 0
    for v in vowels:
        counts = word.count(v)
        count_v = count_v + counts
        
        count_v += word.count(v)
    
    return count_v


text = "Weer een stukje tekst met allemaal klinkers"
list_of_words = text.lower().replace(',','').replace('.', '').split()

print(sorted(list_of_words))
print(sorted(list_of_words, key=number_of_vowels))
