file = open("teams.txt", "w")

team_list = ["Chelsea", "Arsenal", "Man U", "Avengers", "Microsoft Teams"]
for n in range(len(team_list)):
    newline = str(team_list[n]) + "\n"
    file.write(newline)

file.close

file = open("teams.txt", "r")

print(file.readline())
file.readline()

file.close()