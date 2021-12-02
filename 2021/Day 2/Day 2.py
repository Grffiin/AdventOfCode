import sys

sys.setrecursionlimit(2500)


# pos is [hor, depth]
def compute_position(instruction, pos=None):
    if pos is None:
        pos = [0, 0]
    split = instruction.split()
    direction = split[0]
    magnitude = int(split[1])
    switch = {
        'forward': forward,
        'down': down,
        'up': up
    }
    fn = switch.get(direction)
    return fn(magnitude, pos)


def forward(magnitude, pos):
    return [pos[0] + magnitude, pos[1]]


def up(magnitude, pos):
    return [pos[0], pos[1] - magnitude]


def down(magnitude, pos):
    return [pos[0], pos[1] + magnitude]


file = open('Data.txt', 'r')
lines = file.readlines()

cur_pos = compute_position(lines[0])
for i in range(1, len(lines)):
    cur_pos = compute_position(lines[i], cur_pos)

print("FINAL ANSWER DAY 1 PT 1: ", cur_pos[0]*cur_pos[1])