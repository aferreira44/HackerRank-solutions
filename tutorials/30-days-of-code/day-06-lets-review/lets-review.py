n = int(input())
strings = []

for i in range(n):
    strings.append(input())
    s0 = ""
    s1 = ""

    for x in range(len(strings[i])):
        if x % 2 == 0:
            s0 += strings[i][x];
        else:
            s1 += strings[i][x];

    print(s0 + " " + s1)
