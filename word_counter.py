def word_counter(predlozheniye):
    prspl = predlozheniye.split(" ")
    word_count = {'word_count': len(prspl), 'symbol_count': len(predlozheniye)}
    return word_count
predlozheniye = input("vvedite predlozheniye: ")
print(word_counter(predlozheniye))
