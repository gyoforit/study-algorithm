def thuemorse(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x%2:
        return 1-thuemorse(x//2)
    else:
        return thuemorse(x//2)

print(thuemorse(int(input())-1))