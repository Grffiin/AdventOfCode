PasswordRange = [137683, 596253]


class sixNumber:
    array = [0, 0, 0, 0, 0, 0]
    num = 0

    def __init__(self, n):
        self.array = list(map(int, str(n)))
        self.num = n

    # Returns true if adjacency check passes
    def adjacentCheck(self) -> bool:
        double = False
        for x in range(1, 6):
            if self.array[x - 1] > self.array[x]:
                # Fails increasing criteria
                return False
            last = self.array[x]
            if self.array[x] == self.array[x - 1]:
                double = True

        # If reaches this point, increasing criteria is passed; check if we found a double
        return double


def solver():
    found = 0
    for x in range(137684, 596253):
        if sixNumber(x).adjacentCheck():
            found += 1
    print("Valid passwords found: " + str(found))


# solver()

# PART 2

class sixNumberv2:
    array = [0, 0, 0, 0, 0, 0]
    num = 0

    def __init__(self, n):
        self.array = list(map(int, str(n)))
        self.num = n

    # Returns true if adjacency check passes
    def adjacentCheck(self) -> bool:
        double = False
        x = 1
        numCount = {}
        while x in range(1, 6):
            if self.array[x - 1] > self.array[x]:
                # Fails increasing criteria
                return False
            # check for possible double
            if self.array[x] == self.array[x - 1]:
                if self.array[x] in numCount:
                    numCount[self.array[x]] += 1
                else:
                    numCount[self.array[x]] = 2
            x += 1

        # If reaches this point, increasing criteria is passed; check if we found a double
        for x in numCount.values():
            if x == 2:
                return True
        return False


def solverv2():
    found = 0
    for x in range(137684, 596253):
        if sixNumberv2(x).adjacentCheck():
            found += 1
            print("Found: " + str(x))
    print("Valid passwords found: " + str(found))

solverv2()
