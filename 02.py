#Day 02

with open('./02.txt') as myinput:
    spreadsheet = myinput.readlines()

spreadsheet = [list(map(int, i.split())) for i in spreadsheet]

#Part 1

checksum = 0
for line in spreadsheet:
    checksum += max(line) - min(line)

print(checksum)

#Part 2

sorted_spreadsheet = [sorted(i, reverse=True) for i in spreadsheet]

checksum = 0
for line in sorted_spreadsheet:
    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            if line[i] % line[j] == 0:
                checksum += line[i] // line[j]

print(checksum)