# Part 1 solution
with open("C:\\Users\\gmilas\\PycharmProjects\\Advent\\Data\\day1.txt", "r") as file:
    print("Part 1 solution: " + str(sum([int(x) // 3 - 2 for x in file])))


# Part 2 Solution
def solver(inputs):
    # Calculates one 'step' of calculation for each input
    def singleinput(input):
        return max(0, input // 3 - 2)

    RunningTotal = 0
    CurrentList = inputs
    while sum(CurrentList) != 0:
        CurrentList = [singleinput(x) for x in CurrentList]
        RunningTotal += sum(CurrentList)
    return RunningTotal


file = [int(x) for x in open("C:\\Users\\gmilas\\PycharmProjects\\Advent\\Data\\day1.txt", "r")]
print("Part 2 solution: " + str(solver(file)))

