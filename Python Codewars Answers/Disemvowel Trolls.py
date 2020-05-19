def disemvowel(string):
    vowel = "A a E e I i O o U u".split()
    return "".join([i for i in string if not i in vowel])
