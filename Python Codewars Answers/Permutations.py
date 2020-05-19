import itertools
def permutations(string):
    return list("".join(x) for x in set(itertools.permutations(string)))
