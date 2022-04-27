number_of_crimes = input()
crimes = [int(crimes) for crimes in input().split()]
untreated = 0
police_oficers = 0
for i in crimes:
    if i != -1:
        police_oficers += i
    else:
        if police_oficers > 0:
            police_oficers -=1
        else:
            untreated+=1
print(untreated)