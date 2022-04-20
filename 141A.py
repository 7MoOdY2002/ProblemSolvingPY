name1 = str(input())
name2 = str(input())
pile = str(input())
letters_names = {}
letter_pile = {}

for it in name1:
    if it in letters_names:
        letters_names[it] += 1
    else:
        letters_names[it] = 1

for it in name2:
    if it in letters_names:
        letters_names[it] += 1
    else:
        letters_names[it] = 1
for it in pile:
    if it in letter_pile:
        letter_pile[it] += 1
    else:
        letter_pile[it] = 1
possible = 0
if (len(name2) + len(name1) != len(pile)):
    possible = 1
else:
    for key in letters_names:
        if key in letter_pile:
            if letters_names[key] != letter_pile[key]:
                possible = 1
                break
        else:
            possible =1
            break

if possible == 0:
    print("YES")
else:
    print("NO")