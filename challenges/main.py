def has_all_vowels(word):
    required = {"a", "e", "i", "o", "u"}
    word = word.lower()
    #TODO: build a set of vowels actually found in `word`,
    # then check if it `contains all of `required`
    found = {letter for letter in word if letter in required}
    return found == required#if required in word:
        #return True
print(has_all_vowels("education"))