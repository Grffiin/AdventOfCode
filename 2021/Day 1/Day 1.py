import sys
sys.setrecursionlimit(2500)

def check_greater(list, i, last, len):
    if i == len:
        return 0

    cur = int(list[i])
    if cur > last:
        return 1 + check_greater(list, i + 1, cur, len)
    else:
        return check_greater(list, i + 1, cur, len)


file = open('Data.txt', 'r')
lines = file.readlines()

last = int(lines[0])

print(check_greater(lines, 1, last, len(lines)))
