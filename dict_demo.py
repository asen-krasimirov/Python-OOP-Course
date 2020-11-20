contestants = {}
languages = {}

while True:
    command = input()
    if command == "exam finished":
        break

    data = command.split('-')
    username = data[0]
    language = data[1]

    if language == "banned":
        contestants.pop(username)  # remove the contestant they cheat
        continue

    if username not in contestants:
        contestants[username] = 0

    if language not in languages:
        languages[language] = 0

    points = int(data[2])
    if contestants[username] < points:
        contestants[username] = points  # replacing the points if they are bigger

    languages[language] += 1  # adding the submission


sorted_contestants = dict(
    sorted(contestants.items(),
    key=lambda x: (-x[1], x[0])  # in descending order
    )
)

sorted_languages = dict(
    sorted(languages.items(),
    key=lambda x: (-x[1], x[0]) # in descending order
    )
)

print("Results:")
for contestant, points in sorted_contestants.items():
    print(f"{contestant} | {points}")

print("Submissions:")
for language, submissions in sorted_languages.items():
    print(f"{language} - {submissions}")
