

def is_prime(num):
    if num != 0 and num != 1:
        if num % num == 0 and num % 1 == 0:
            for n in range(2, 10):
                if num != n and num % n == 0:
                    return False
            return True
    return False


def get_primes(integers: list):

    for num in integers:
        if is_prime(num):
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))