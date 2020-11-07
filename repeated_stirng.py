

def find_a_in_infinite_string(string: str, repeated_times):
    if repeated_times <= 1_000_000_000:
        string *= repeated_times
        while len(string) > repeated_times:
            string = string[:-1]
        return string.count('a')


data = input()
n = int(input())

print(find_a_in_infinite_string(data, n))
