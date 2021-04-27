import student_code

class bcolors:
	RED    = "\x1b[31m"
	GREEN  = "\x1b[32m"
	NORMAL = "\x1b[0m"

def init_board():
	return [[0 for x in range(0,10)] for x in range(0,10)]
	
	
def set_board(board, data):
	for y in range(0,10):
		for x in range(0,10):
			board[y][x]=int(data[y*10+x])

def check_result(map1, map2):
	result=True
	
	for y in range(0,10):
		v=""
		for x in range(0,10):
			if (map1[y][x]==map2[y][x]):
				v+=bcolors.GREEN+str(map1[y][x])+bcolors.NORMAL+' '
			else:
				result = False
				v+=bcolors.RED+str(map1[y][x])+bcolors.NORMAL+' '
		print(v)
	if (result):
		print("Test Result: " + bcolors.GREEN+"Passed"+bcolors.NORMAL)
	else:
		print("Test Result: " + bcolors.RED+"Failed"+bcolors.NORMAL)
	print()
	return result
	
result=0	
	
data1 = ("1111111111"
"0000000000"
"0000000000"
"0000000000"
"0000000000"
"0000000000"
"0000000000"
"0000000000"
"0000000000"
"0000000000")
			  
result1 = (
"0000000001"
"0000100000"
"0000001000"
"0000000010"
"1000000000"
"0010000000"
"0000000100"
"0000010000"
"0001000000"
"0100000000")
					 
data2  = (
"1000000000"
"0100000000"
"0010000000"
"0001000000"
"0000100000"
"0000010000"
"0000001000"
"0000000100"
"0000000010"
"0000000001")
					 

result2 = (
"0110000000"
"0000000000"
"0000010000"
"0000000100"
"0000000001"
"0001000000"
"0000001000"
"0000100000"
"0000000010"
"1000000000")
			  
			  
			  
			  
data3  = (
"0000000000"
"1000000011"
"0000000000"
"0010010000"
"0000000100"
"0100000000"
"0000000000"
"0001100000"
"0000000000"
"0000001000")

result3 =(
"0000100000"
"0000000010"
"0001000000"
"0000010001"
"0000000100"
"0100000000"
"0000000000"
"1000000000"
"0010000000"
"0000001000")


data4 =("0000000000"
"1001001001"
"0100100100"
"0010010010"
"0000000000"
"0000000000"
"0000000000"
"0000000000"
"0000000000"
"0000000000")

result4 =("1000000000"
"0000000001"
"0000110000"
"0000000010"
"0100000000"
"0000000000"
"0000000100"
"0010000000"
"0000001000"
"0001000000")

data5 =(
"0000000000"
"1000000000"
"0100100000"
"0010010010"
"0000000100"
"0001000000"
"0000000000"
"0000001000"
"0000000000"
"0000000001")

result5 =(
"0000010000"
"0000000010"
"0000100000"
"1000000000"
"0000000100"
"0001000000"
"0100000000"
"0000001000"
"0010000000"
"0000000001")

data6 =("0000000100"
"0000000000"
"0000100000"
"0010000010"
"1000000000"
"0000010000"
"0001000000"
"0100000000"
"0000001001"
"0000000000")


result6 =("0000000100"
"0000000000"
"0000100000"
"0010000010"
"1000000000"
"0000010000"
"0001000000"
"0100000000"
"0000001001"
"0000000000")


all_passed = True
print("testing board 1")
board1 = init_board();
solution1 = init_board();
set_board(board1, data1)
set_board(solution1, result1)
df1 = student_code.gradient_search(board1)
if df1==True:
	print( bcolors.RED+"test return bad"+bcolors.NORMAL)
	result=0
elif df1==False:
	print( bcolors.GREEN+"test return good"+bcolors.NORMAL)
	result=result+1
else:
	print( bcolors.RED+"test return bad"+bcolors.NORMAL)
	result=0
result=result+check_result(solution1,board1)


print("testing board 2")
board1 = init_board();
solution1 = init_board();
set_board(board1, data2)
set_board(solution1, result2)
df1 = student_code.gradient_search(board1)
if df1==True:
	print( bcolors.RED+"test return bad"+bcolors.NORMAL)
	result=0
elif df1==False:
	print( bcolors.GREEN+"test return good"+bcolors.NORMAL)
	result=result+1
else:
	print( bcolors.RED+"test return bad"+bcolors.NORMAL)
	result=0
result=result+check_result(solution1,board1)


print("testing board 3")
board1 = init_board();
solution1 = init_board();
set_board(board1, data3)
set_board(solution1, result3)
df1 = student_code.gradient_search(board1)
if df1==True:
	print( bcolors.RED+"test return bad"+bcolors.NORMAL)
	result=0
elif df1==False:
	print( bcolors.GREEN+"test return good"+bcolors.NORMAL)
	result=result+1
else:
	print( bcolors.RED+"test return bad"+bcolors.NORMAL)
	result=0
result=result+check_result(solution1,board1)


print("testing board 4")
board1 = init_board();
solution1 = init_board();
set_board(board1, data4)
set_board(solution1, result4)
df1 = student_code.gradient_search(board1)
if df1==True:
	print( bcolors.RED+"test return bad"+bcolors.NORMAL)
	result=0
elif df1==False:
	print( bcolors.GREEN+"test return good"+bcolors.NORMAL)
	result=result+1
else:
	print( bcolors.RED+"test return bad"+bcolors.NORMAL)
	result=0
result=result+check_result(solution1,board1)


print("testing board 5")
board1 = init_board();
solution1 = init_board();
set_board(board1, data5)
set_board(solution1, result5)
df1 = student_code.gradient_search(board1)
if df1==False:
	print( bcolors.RED+"test return bad"+bcolors.NORMAL)
	result=0
elif df1==True:
	print( bcolors.GREEN+"test return good"+bcolors.NORMAL)
	result=result+1
else:
	print( bcolors.RED+"test return bad"+bcolors.NORMAL)
	result=0
result=result+check_result(solution1,board1)




print("testing board 6")
board1 = init_board();
solution1 = init_board();
set_board(board1, data6)
set_board(solution1, result6)
df1 = student_code.gradient_search(board1)
if df1==True:
	print( bcolors.RED+"test return bad"+bcolors.NORMAL)
	result=0
elif df1==False:
	print( bcolors.GREEN+"test return good"+bcolors.NORMAL)
	result=result+1
else:
	print( bcolors.RED+"test return bad"+bcolors.NORMAL)
	result=0
result=result+check_result(solution1,board1)


if result==12:
	print( bcolors.GREEN+"all tests passed"+bcolors.NORMAL)
else:
	print( bcolors.RED+"test fail"+bcolors.NORMAL)

