import random
import math

def calculate():

	global city
	global order

	dis = 0
	for i in range(0,17):
		dis += int(city[order[i]][order[i+1]])
	return dis

if __name__ == "__main__":

	global n
	global t1
	global alpha
	global n_max
	global city
	global order

	#initialize parameter
	n = 0
	t = 500
	alpha = 0.995
	n_max = 100000
	city = [[0]*17]*17
	order = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,0]
	tmp = order

	#read file into matrix
	f = open("gr17_d.txt","r")
	line = f.readline()
	line = line.strip().split()
	row = 0
	while line:
		city[row] = line
		line = f.readline()
		line = line.strip().split()
		row += 1
		if row == 18:
			break
	f.close()
	# SA simulating
	min = 9999
	while(n < n_max):
		fx = calculate()
		rand1 = random.randint(0,16)
		rand2 = random.randint(0,16)
		while rand1 == rand2 :
			rand2 = random.randint(0,16)
		temp = order[rand1]
		order[rand1] = order[rand2]
		order[rand2] = temp
		if rand1 == 0 or rand2 == 0:
			order[17] = order[0]
		if fx < min :
			min = fx
			tmp = order
		else :
			order = tmp
			if random.random() <= math.exp((min-fx)/t) :
				min = fx
				tmp = order
		n += 1
		t *= alpha
	# print result
	print(min)
	print(order)
