import sys

sys.setrecursionlimit(2500)


# i=0: A
# i=1: A B ] OVERLAP
# i=2: A B ] OVERLAP
# i=3:   B
#

# A = list[i-1] + list[i] + list[i+1]
# B =             list[i] + list[i+1] + list[i+2]

# B-A = list[i+2]-list[i-1]



def check_greater(list, i, last, len):
    if i == len-2:
        return 0

    cur = int(lines[i+2])
    if cur > last:
        return 1 + check_greater(list, i + 1, int(list[i]), len)
    else:
        return check_greater(list, i + 1, int(list[i]), len)


file = open('Data.txt', 'r')
lines = file.readlines()

last = int(lines[0])

print(check_greater(lines, 1, last, len(lines)))
