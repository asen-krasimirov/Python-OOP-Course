GROWING = 1
SHRINKING = -1


def print_rhombus(n):
    def print_line(i, direction):
        i += direction
        if i == 0:
            return

        if i > n:
            print_line(i-1, SHRINKING)
            return

        line = ' ' * (n-i) + '* ' * i
        print(line.rstrip())
        print_line(i, direction)

    print_line(0, GROWING)


size = int(input())
print_rhombus(size)