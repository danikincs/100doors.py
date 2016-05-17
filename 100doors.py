list = [0 * x for x in range(101)]
print("The following doors are open:")
for b in range(1,101):
    for a in range(1,101):
        if a % b == 0:
            if list[a] == 0:
                list[a] = 1
            else:
                list[a] = 0
for c in range(100):
    if list[c] == 1:
        print (c)
