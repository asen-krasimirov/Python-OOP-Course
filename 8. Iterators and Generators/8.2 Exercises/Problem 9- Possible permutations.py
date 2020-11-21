from itertools import permutations


def possible_permutations(number_list: list):
    for permutation in permutations(number_list):
        yield list(permutation)


[print(n) for n in possible_permutations([1, 2, 3])]