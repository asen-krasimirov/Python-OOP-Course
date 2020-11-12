

def create_files():
    files = input().split(', ')

    for file in files:
        with open(file, 'x'):
            pass
