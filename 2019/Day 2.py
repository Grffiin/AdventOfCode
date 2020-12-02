class IntCodeSolver:
    # Calls the helper, which runs the majority of the code
    def intCodeSolver(self, intcode):
        return self.intCodeStepper(intcode, 0)

    # Performs one step of the IntCode
    def intCodeStepper(self, intcode, headloc):
        opcode = intcode[headloc]
        if opcode == 99:
            return intcode
        methodName = "opcode_" + str(intcode[headloc])
        toCall = getattr(self, methodName, self.opcode_error)
        return toCall(intcode, headloc)

    # Adds numbers in next 2 positions after head, and stores it in the following position
    def opcode_1(self, intcode, headloc):
        newIntcode = intcode
        newIntcode[newIntcode[headloc + 3]] = newIntcode[newIntcode[headloc + 1]] + newIntcode[newIntcode[headloc + 2]]
        return self.intCodeStepper(newIntcode, headloc + 4)

    # Multiplies numbers in next 2 positions after head, and stores it in the following position
    def opcode_2(self, intcode, headloc):
        newIntcode = intcode
        newIntcode[newIntcode[headloc + 3]] = newIntcode[newIntcode[headloc + 1]] * newIntcode[newIntcode[headloc + 2]]
        return self.intCodeStepper(newIntcode, headloc + 4)

    def opcode_error(self, intcode, headloc):
        return ["Error!"]


toSolve = [1, 12, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 6, 19, 1, 9, 19, 23, 2, 23,
           10, 27, 1, 27, 5, 31, 1, 31, 6, 35, 1, 6, 35, 39, 2, 39, 13, 43, 1, 9, 43, 47, 2,
           9, 47, 51, 1, 51, 6, 55, 2, 55, 10, 59, 1, 59, 5, 63, 2, 10, 63, 67, 2, 9, 67, 71,
           1, 71, 5, 75, 2, 10, 75, 79, 1, 79, 6, 83, 2, 10, 83, 87, 1, 5, 87, 91, 2, 9, 91,
           95, 1, 95, 5, 99, 1, 99, 2, 103, 1, 103, 13, 0, 99, 2, 14, 0, 0]
s = IntCodeSolver()
# print(IntCodeSolver.intCodeSolver(s, toSolve))

# PART 2 SOLUTION

baseList = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 6, 19, 1, 9, 19, 23, 2, 23, 10, 27, 1, 27, 5, 31, 1,
            31, 6, 35, 1, 6, 35, 39, 2, 39, 13, 43, 1, 9, 43, 47, 2, 9, 47, 51, 1, 51, 6, 55, 2, 55, 10, 59, 1, 59, 5,
            63, 2, 10, 63, 67, 2, 9, 67, 71, 1, 71, 5, 75, 2, 10, 75, 79, 1, 79, 6, 83, 2, 10, 83, 87, 1, 5, 87, 91, 2,
            9, 91, 95, 1, 95, 5, 99, 1, 99, 2, 103, 1, 103, 13, 0, 99, 2, 14, 0, 0]

import copy

def solver():
    print("INITIAL LIST")
    print(baseList)
    for x in range(0, 100):
        for y in range(0, 100):
            toCheck = copy.deepcopy(baseList)
            toCheck[1] = x
            toCheck[2] = y
            print("Checking: " + str(x) + " " + str(y))
            print(toCheck)
            solved = IntCodeSolver.intCodeSolver(s, toCheck)
            if solved[0] == 19690720:
                print("Noun is: " + str(x))
                print("Verb is: " + str(y))
                print("Program answer is: " + str(100 * x + y))
                return
    print("Well, that didn't work")
    return


solver()
