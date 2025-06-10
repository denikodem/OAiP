#     Сколько гласных в тексте      #
# RU - а, е, ё, и, о, у, ы, э, ю, я #
# EN - a, e, i, o, u                #
# DE - a, e, i, o, u, ä, ö, ü       #


def count_vowels(text, vowels):
    return sum(1 for c in text.lower() if c in vowels)
