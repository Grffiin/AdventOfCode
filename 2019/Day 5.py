# TODO: fix auto-increase

class IntCodeSolver:
    # Calls the helper, which runs the majority of the code
    def intCodeSolver(self, intcode):
        return self.intCodeStepper(intcode, 0)

    # Performs one step of the IntCode
    def intCodeStepper(self, intcode, headloc):
        opcode = intcode[headloc]
        # Convert opcode to list of ints
        intcodeList = list(map(int, str(opcode)))
        # Pad the opCode with 0's, if necessary
        if len(intcodeList) < 2:
            intcodeList.insert(0, 0)
        # Re-convert 2-digit opcode into single number
        opcode = intcodeList[-1] + (10 * intcodeList[-2])
        # Check if this is the exit code
        if opcode == 99:
            return intcode
        # Retrive opcode class and get numParams
        opClass = getattr(self, "opcode_" + str(opcode), self.opcode_error)
        numParams = opClass.numParams
        # Pad intCodeList with 0's, if necessary
        while len(intcodeList) - 2 < numParams:
            intcodeList.insert(0, 0)
        # retrive the parameters to send to the opcode class
        paramList = []
        for x in range(0, numParams):
            currentParam = intcodeList[x]
            paramcodeClass = getattr(self, "param_" + str(currentParam), "param_error")
            paramList.insert(0, paramcodeClass.getParam(self, intcode, headloc, numParams - x))
        # send parameters to opcode class to execute
        intcode = opClass.perform(self, intcode, paramList)
        return self.intCodeStepper(intcode, headloc + 1 + numParams)

    # poition parameter
    class param_0:
        def getParam(self, intcode, headloc, instrIndex):
            return intcode[headloc + instrIndex]

    # immediate parameter
    class param_1:
        def getParam(self, intcode, headloc, instrIndex):
            return headloc + instrIndex

    # error parameter
    class param_error:
        def getParam():
            return "ERROR"

    # Adds numbers
    class opcode_1:
        numParams = 3

        def perform(self, intcode, params):
            intcode[params[2]] = intcode[params[0]] + intcode[params[1]]
            return intcode

    # Multiplies numbers
    class opcode_2:
        numParams = 3

        def perform(self, intcode, params):
            intcode[params[2]] = intcode[params[0]] * intcode[params[1]]
            return intcode

    # Stores user input in given location
    class opcode_3:
        numParams = 1

        def perform(self, intcode, params):
            intcode[params[0]] = int(input("Input Requested: "))
            return intcode

    # Prints value at a location
    class opcode_4:
        numParams = 1

        def perform(self, intcode, params):
            print(intcode[params[0]])
            return intcode

    # jump if true
    class opcode_5:
        numParams = 2

        # if 1st param is non-zero, instruction pointer set to 2nd param
        def perform(self, intcode, params):
            if intcode[params[0]] != 0:
                intcode[params[0] - 1] = intcode[params[1]]

    # jump if false
    class opcode_6:
        numParams = 2

        # if 1st param is non-zero, instruction pointer set to 2nd param
        def perform(self, intcode, params):
            if intcode[params[0]] == 0:
                intcode[params[0] - 1] = intcode[params[1]]

    # less than
    class opcode_7:
        numParams = 3

        def perform(self, intcode, params):
            if intcode[params[0]] < intcode[params[1]]:
                intcode[params[2]] = 1
            else:
                intcode[params[2]] = 0

    # equals
    class opcode_8:
        numParams = 3

        def perform(self, intcode, params):
            if intcode[params[0]] == intcode[params[1]]:
                intcode[params[2]] = 1
            else:
                intcode[params[2]] = 0




    # Error code
    class opcode_error:
        numParams = 0

        def perform(self, intcode, headloc):
            return ["Error!"]


s = IntCodeSolver()
x = s.intCodeSolver(
    [3, 225, 1, 225, 6, 6, 1100, 1, 238, 225, 104, 0, 1101, 61, 45, 225, 102, 94, 66, 224, 101, -3854, 224, 224, 4, 224,
     102, 8, 223, 223, 1001, 224, 7, 224, 1, 223, 224, 223, 1101, 31, 30, 225, 1102, 39, 44, 224, 1001, 224, -1716, 224,
     4, 224, 102, 8, 223, 223, 1001, 224, 7, 224, 1, 224, 223, 223, 1101, 92, 41, 225, 101, 90, 40, 224, 1001, 224,
     -120, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 1, 224, 1, 223, 224, 223, 1101, 51, 78, 224, 101, -129, 224, 224,
     4, 224, 1002, 223, 8, 223, 1001, 224, 6, 224, 1, 224, 223, 223, 1, 170, 13, 224, 101, -140, 224, 224, 4, 224, 102,
     8, 223, 223, 1001, 224, 4, 224, 1, 223, 224, 223, 1101, 14, 58, 225, 1102, 58, 29, 225, 1102, 68, 70, 225, 1002,
     217, 87, 224, 101, -783, 224, 224, 4, 224, 102, 8, 223, 223, 101, 2, 224, 224, 1, 224, 223, 223, 1101, 19, 79, 225,
     1001, 135, 42, 224, 1001, 224, -56, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 6, 224, 1, 224, 223, 223, 2, 139,
     144, 224, 1001, 224, -4060, 224, 4, 224, 102, 8, 223, 223, 101, 1, 224, 224, 1, 223, 224, 223, 1102, 9, 51, 225, 4,
     223, 99, 0, 0, 0, 677, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1105, 0, 99999, 1105, 227, 247, 1105, 1, 99999, 1005, 227,
     99999, 1005, 0, 256, 1105, 1, 99999, 1106, 227, 99999, 1106, 0, 265, 1105, 1, 99999, 1006, 0, 99999, 1006, 227,
     274, 1105, 1, 99999, 1105, 1, 280, 1105, 1, 99999, 1, 225, 225, 225, 1101, 294, 0, 0, 105, 1, 0, 1105, 1, 99999,
     1106, 0, 300, 1105, 1, 99999, 1, 225, 225, 225, 1101, 314, 0, 0, 106, 0, 0, 1105, 1, 99999, 1008, 677, 226, 224,
     102, 2, 223, 223, 1006, 224, 329, 101, 1, 223, 223, 108, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 344, 101, 1,
     223, 223, 107, 677, 677, 224, 1002, 223, 2, 223, 1005, 224, 359, 101, 1, 223, 223, 1107, 226, 677, 224, 1002, 223,
     2, 223, 1005, 224, 374, 1001, 223, 1, 223, 1008, 677, 677, 224, 102, 2, 223, 223, 1006, 224, 389, 1001, 223, 1,
     223, 1007, 677, 677, 224, 1002, 223, 2, 223, 1006, 224, 404, 1001, 223, 1, 223, 8, 677, 226, 224, 102, 2, 223, 223,
     1005, 224, 419, 1001, 223, 1, 223, 8, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 434, 101, 1, 223, 223, 1107, 226,
     226, 224, 1002, 223, 2, 223, 1006, 224, 449, 101, 1, 223, 223, 1107, 677, 226, 224, 102, 2, 223, 223, 1005, 224,
     464, 101, 1, 223, 223, 1108, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 479, 1001, 223, 1, 223, 7, 677, 677, 224,
     1002, 223, 2, 223, 1006, 224, 494, 101, 1, 223, 223, 7, 677, 226, 224, 102, 2, 223, 223, 1005, 224, 509, 101, 1,
     223, 223, 1108, 226, 677, 224, 1002, 223, 2, 223, 1006, 224, 524, 101, 1, 223, 223, 8, 226, 677, 224, 1002, 223, 2,
     223, 1005, 224, 539, 101, 1, 223, 223, 1007, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 554, 1001, 223, 1, 223,
     108, 226, 226, 224, 1002, 223, 2, 223, 1006, 224, 569, 1001, 223, 1, 223, 1108, 677, 226, 224, 102, 2, 223, 223,
     1005, 224, 584, 101, 1, 223, 223, 108, 226, 677, 224, 102, 2, 223, 223, 1005, 224, 599, 101, 1, 223, 223, 1007,
     226, 677, 224, 102, 2, 223, 223, 1006, 224, 614, 1001, 223, 1, 223, 1008, 226, 226, 224, 1002, 223, 2, 223, 1006,
     224, 629, 1001, 223, 1, 223, 107, 226, 226, 224, 1002, 223, 2, 223, 1006, 224, 644, 101, 1, 223, 223, 7, 226, 677,
     224, 102, 2, 223, 223, 1005, 224, 659, 1001, 223, 1, 223, 107, 677, 226, 224, 102, 2, 223, 223, 1005, 224, 674,
     1001, 223, 1, 223, 4, 223, 99, 226])

print("Final output: " + str(x))
