#Day 04

with open('./04.txt') as myinput:
    passphrases = myinput.readlines()

valid_1, valid_2 = 0, 0
for passphrase in passphrases:
    passwords = passphrase.split()
    if len(passwords) == len(set(passwords)):
        valid_1 += 1
        passwords_sorted = set()
        for password in passwords:
            passwords_sorted.add(''.join(sorted(password)))
        if len(passwords) == len(set(passwords_sorted)):
            valid_2 += 1

#Part 1

print(valid_1)

#Part 2

print(valid_2)