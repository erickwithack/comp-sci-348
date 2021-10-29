import common
import student_code


class bcolors:
    RED = "\x1b[31m"
    GREEN = "\x1b[32m"
    NORMAL = "\x1b[0m"


def run_experiment(board, next, win, gmme, gabe):
    b = [0 for x in range(9)]
    common.set_board(b, board)
    common.print_board(b)
    common.variables.explored = 0
    wmm = student_code.minmax_tictactoe(b, next)
    mme = common.variables.explored
    common.variables.explored = 0
    wabp = student_code.abprun_tictactoe(b, next)
    abpe = common.variables.explored

    print(common.legend(next) + " moves Result :")
    res1 = "- MIN-MAX: " + common.legend(wmm) + " wins "
    if (wmm != win):
        res1 += "(" + bcolors.RED + "Fail" + bcolors.NORMAL + ")"
    else:
        res1 += "(" + bcolors.GREEN + "Pass" + bcolors.NORMAL + ")"

    res1 += " boards explored " + str(mme)

    if (mme != gmme):
        res1 += "(" + bcolors.RED + "Fail" + bcolors.NORMAL + ")"
    else:
        res1 += "(" + bcolors.GREEN + "Pass" + bcolors.NORMAL + ")"

    print(res1)

    res1 = "- ALPHA-BETA: "+common.legend(wabp)+" wins "
    if (wabp != win):
        res1 += "(" + bcolors.RED + "Fail" + bcolors.NORMAL + ")"
    else:
        res1 += "(" + bcolors.GREEN + "Pass" + bcolors.NORMAL + ")"

    res1 += " boards explored " + str(abpe)

    if (abpe != gabe):
        res1 += "(" + bcolors.RED + "Fail" + bcolors.NORMAL + ")"
    else:
        res1 += "(" + bcolors.GREEN + "Pass" + bcolors.NORMAL + ")"

    print(res1)
    print("")
    print("")
    return wmm == win and mme <= gmme and wabp == win and abpe <= gabe


board1 = (
    "O X"
    "XXO"
    "OX ")
next1 = common.constants.X
win1 = common.constants.X
mme1 = 4
abe1 = 4

board2 = (
    " OX"
    "   "
    "   ")
next2 = common.constants.X
win2 = common.constants.X
mme2 = 8232
abe2 = 880

board3 = (
    "OXX"
    "OO "
    "   ")
next3 = common.constants.X
win3 = common.constants.O
mme3 = 27
abe3 = 13

board4 = (
    "O  "
    " X "
    "   ")
next4 = common.constants.X
win4 = common.constants.NONE
mme4 = 6812
abe4 = 703

board5 = (
    "XXO"
    "OXX"
    "OXO")
next5 = common.constants.X
win5 = common.constants.X
mme5 = 1
abe5 = 1

board6 = (
    "OXX"
    "XO "
    "XOO")
next6 = common.constants.X
win6 = common.constants.O
mme6 = 1
abe6 = 1


board7 = (
    "   "
    "   "
    "   ")
next7 = common.constants.X
win7 = common.constants.NONE
mme7 = 549946
abe7 = 18297


board8 = (
    "OOO"
    "OO "
    "OOO")
next8 = common.constants.X
win8 = common.constants.O
mme8 = 1
abe8 = 1
all_passed = True
all_passed = all_passed

print("Board 1")
exp1 = run_experiment(board1, next1, win1, mme1, abe1)
print("Board 2")
exp2 = run_experiment(board2, next2, win2, mme2, abe2)
print("Board 3")
exp3 = run_experiment(board3, next3, win3, mme3, abe3)
print("Board 4")
exp4 = run_experiment(board4, next4, win4, mme4, abe4)
print("Board 5")
exp5 = run_experiment(board5, next5, win5, mme5, abe5)
print("Board 6")
exp6 = run_experiment(board6, next6, win6, mme6, abe6)
print("Board 7")
exp7 = run_experiment(board7, next7, win7, mme7, abe7)
print("Board 8")
exp8 = run_experiment(board8, next8, win8, mme8, abe8)

all_passed = exp1 and exp2 and exp3 and exp4 and exp5 and exp6 and exp7


if all_passed:
    exit(0)
else:
    exit(1)
