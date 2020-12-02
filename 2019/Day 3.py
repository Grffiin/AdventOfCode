def manhattan(p1: tuple, p2: tuple) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


class wireSolver:
    def solve(self, file):
        # Read lines from the file
        lines = file.readlines()
        wire1 = self.tracer(lines[0])
        wire2 = self.tracer(lines[1])
        crosses = set(wire1) & set(wire2)
        crosses.discard((0, 0))
        print("Answer is: " + str(min(manhattan(cross, (0, 0)) for cross in crosses)))

    def tracer(self, instrStr: str):
        points = [(0, 0)]
        instrList = instrStr.split(",")
        for instr in instrList:
            points = points + self.instructionParser(instr, points[-1])
        return points

    def instructionParser(self, instr: str, start: tuple):
        magnitude = int(instr[1:])
        direction = instr[0]

        startX = start[0]
        startY = start[1]

        if direction == "L":
            line = [(startX - i, startY) for i in range(1, magnitude + 1)]
        if direction == "R":
            line = [(startX + i, startY) for i in range(1, magnitude + 1)]
        if direction == "U":
            line = [(startX, startY + i) for i in range(1, magnitude + 1)]
        if direction == "D":
            line = [(startX, startY - i) for i in range(1, magnitude + 1)]

        return line


w = wireSolver()


# with open("C:\\Users\\gmilas\\PycharmProjects\\Advent\\Data\\day3.txt", "r") as file:
#     wireSolver.solve(w, file)


## PART 2

class wireSolver2:
    def solve(self, file):
        # Read lines from the file
        lines = file.readlines()
        wire1 = self.tracer(lines[0])
        wire2 = self.tracer(lines[1])
        crosses = set(wire1) & set(wire2)
        crosses.discard((0, 0))
        crossesDistanceSet = {pt: wire1.index(pt) + wire2.index(pt) for pt in crosses}
        print(crossesDistanceSet)
        print(str(min(x for x in crossesDistanceSet.values())))


    def tracer(self, instrStr: str):
        points = [(0, 0)]
        instrList = instrStr.split(",")
        for instr in instrList:
            points = points + self.instructionParser(instr, points[-1])
        return points

    def instructionParser(self, instr: str, start: tuple):
        magnitude = int(instr[1:])
        direction = instr[0]

        startX = start[0]
        startY = start[1]

        if direction == "L":
            line = [(startX - i, startY) for i in range(1, magnitude + 1)]
        if direction == "R":
            line = [(startX + i, startY) for i in range(1, magnitude + 1)]
        if direction == "U":
            line = [(startX, startY + i) for i in range(1, magnitude + 1)]
        if direction == "D":
            line = [(startX, startY - i) for i in range(1, magnitude + 1)]

        return line


with open("C:\\Users\\gmilas\\PycharmProjects\\Advent\\Data\\day3.txt", "r") as file:
    wireSolver2.solve(w, file)
