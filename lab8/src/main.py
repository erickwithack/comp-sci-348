import common
import student_code
import array

class bcolors:
	RED    = "\x1b[31m"
	GREEN  = "\x1b[32m"
	NORMAL = "\x1b[0m"
	
def read_data(training_data,test_data1,gold_data1,filename):
	data = array.array('f')
	test = array.array('f')
	
	with open(filename, 'rb') as fd:
		data.fromfile(fd, common.constants.TRAINING_SIZE*(common.constants.DATA_DIM+1))
		test.fromfile(fd, common.constants.TEST_SIZE*(common.constants.DATA_DIM+1))

	for i in range(common.constants.TRAINING_SIZE):
		for j in range(common.constants.DATA_DIM+1):
			training_data[i][j]=data[i*(common.constants.DATA_DIM+1)+j] 
			
	for i in range(common.constants.TEST_SIZE):
		for j in range(common.constants.DATA_DIM):
			test_data1[i][j]=test[i*(common.constants.DATA_DIM+1)+j] 
		test_data1[i][common.constants.DATA_DIM]=-1
		gold_data1[i]=test[i*(common.constants.DATA_DIM+1)+common.constants.DATA_DIM]
	f = open(filename.split('.dat')[0] + '.csv', 'w')
	for i in training_data:
		f.write(str(i[0]) + ',' + str(i[1]) + ',' + str(i[2]) + '\n')
	for i in range(len(test_data1)):
		f.write(str(test_data1[i][0]) + ',' + str(test_data1[i][1]) + ',' + str(gold_data1[i]) + '\n')
	f.close()

def read_data_csv(training_data,test_data1,gold_data1,filename):
	data = []	
	test = []
	with open(filename, 'r') as fd:
                lines = fd.readlines()
                for i in range(common.constants.TRAINING_SIZE + common.constants.TEST_SIZE):
                    if i < common.constants.TRAINING_SIZE:
                        data += [float(j) for j in lines[i].strip().split(',')]
                    else:
                        test += [float(j) for j in lines[i].strip().split(',')]

	for i in range(common.constants.TRAINING_SIZE):
		for j in range(common.constants.DATA_DIM+1):
			training_data[i][j]=data[i*(common.constants.DATA_DIM+1)+j] 
			
	for i in range(common.constants.TEST_SIZE):
		for j in range(common.constants.DATA_DIM):
			test_data1[i][j]=test[i*(common.constants.DATA_DIM+1)+j] 
		test_data1[i][common.constants.DATA_DIM]=-1
		gold_data1[i]=test[i*(common.constants.DATA_DIM+1)+common.constants.DATA_DIM]


def run_experiment1(filename):
	gold_data = [0 for x in range(common.constants.TEST_SIZE)]
	test_data = [[0, 0, 0] for x in range(common.constants.TEST_SIZE)]
	training_data = [[0, 0, 0] for x in range(common.constants.TRAINING_SIZE)]
	#generating data should be hidden from students!
	read_data_csv(training_data,test_data,gold_data,filename)

	#this is one of the two student functions
	#print (training_data)#, test_data, gold_data)
	student_code.part_one_classifier(training_data,test_data)
	#part 1 grading
	error=0
	for i in range(common.constants.TEST_SIZE):
		if(test_data[i][common.constants.DATA_DIM]!=gold_data[i]):
			error+=1
	
	print ("Incorrect classification is "+str(error)+" out of " + str(common.constants.TEST_SIZE))

	success=True
	
	if (error<=float(common.constants.TEST_SIZE)*.05):
		print("("+ bcolors.GREEN + "SUCCESS" + bcolors.NORMAL + ")")
	else:
		success=False;
		print( "(" + bcolors.RED + "FAIL" + bcolors.NORMAL + ") maximum "+ str(float(common.constants.TEST_SIZE)*.05))

	print
	return success
	

def run_experiment2(filename):
	gold_data = [0 for x in range(common.constants.TEST_SIZE)]
	test_data = [[0, 0, 0] for x in range(common.constants.TEST_SIZE)]
	training_data = [[0, 0, 0] for x in range(common.constants.TRAINING_SIZE)]

	#generating data should be hidden from students!
	read_data_csv(training_data,test_data,gold_data,filename)
	#this is one of the two student functions
	student_code.part_two_classifier(training_data,test_data);
	#part 2 grading

	error=0
	for i in range(common.constants.TEST_SIZE):
		if(test_data[i][common.constants.DATA_DIM]!=gold_data[i]):
			# print("error is data", test_data[i])
			error+=1
	
	print ("Incorrect classification is "+str(error)+" out of " + str(common.constants.TEST_SIZE))

	success=True

	if (error<=float(common.constants.TEST_SIZE)*.05):
		print( "("+ bcolors.GREEN + "SUCCESS" + bcolors.NORMAL + ")")
	else:
		success=False;
		print ("(" + bcolors.RED + "FAIL" + bcolors.NORMAL + ") maximum "+ str(float(common.constants.TEST_SIZE)*.05))

	print
	return success

all_passed=True

filename1 = "../data1.csv"
print("Linear Classifier : Dataset 1")
all_passed=run_experiment1(filename1) and all_passed
filename2 = "../data2.csv"
print ("Linear Classifier : Dataset 2")
all_passed=run_experiment1(filename2) and all_passed
filename3 = "../data3.csv"
print ("Linear Classifier : Dataset 3")
all_passed=run_experiment1(filename3) and all_passed
filename4 = "../data4.csv"
print ("Linear Classifier : Dataset 4")
all_passed=run_experiment1(filename4) and all_passed

filename5 = "../datar1.csv"
print( "Accelerometer : Dataset 1")
all_passed=run_experiment2(filename5) and all_passed
filename6 = "../datar2.csv"
print( "Accelerometer : Dataset 2")
all_passed=run_experiment2(filename6) and all_passed
filename7 = "../datar3.csv"
print( "Accelerometer : Dataset 3")
all_passed=run_experiment2(filename7) and all_passed

 
if all_passed:
	exit(0)
else:
	exit(1)
