

def vowel_filter(function):

    def wrapper():
        result = function()
        return [char for char in result if char in 'aeiouy']

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


def test():
    result = get_letters()
    assert result == ["a", "e"], result
    print('success')


if __name__ == '__main__':
    test()
