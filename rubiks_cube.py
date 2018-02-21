from sys import argv

initial_mix = int(argv[1])


import random

solved = False
correct_sides = 0


# the starting cube, solved

front = ['R','R','R','R','R','R','R','R','R']
left = ['B','B','B','B','B','B','B','B','B']
right = ['Y','Y','Y','Y','Y','Y','Y','Y','Y']
back = ['G','G','G','G','G','G','G','G','G']
top = ['W','W','W','W','W','W','W','W','W']
bottom = ['O','O','O','O','O','O','O','O','O']


# these lists will be the cube after a turn

new_front = []
new_left = []
new_right = []
new_back = []
new_top = []
new_bottom = []


# list with all old and new faces.  On a turn, the new face will become the next member
# in the list.  For example, on vert_down, in the column that is spun, the new front will
# be whatever was on top.  

vert_down = [new_front, top, new_top, back, new_back, bottom, new_bottom, front,new_left,left,new_right,right]
vert_up = [new_front, bottom, new_bottom, back, new_back, top, new_top, front,new_left,left,new_right,right]
hor_right = [new_front, left, new_left, back, new_back, right, new_right, front,new_top,top,new_bottom,bottom]
hor_left = [new_front, right, new_right, back, new_back, left, new_left, front,new_top,top,new_bottom,bottom]


# Which squares get changed depending on which action is done.  For example, spinning the 
# first column affects squares 0, 3 and 6 (in python counting)

# Numbering is as follows...
#     1: spin column 1 down 
#     2: spin column 2 down
#     3: spin column 3 down
#     4: spin column 1 up
#     5: spin column 2 up
#     6: spin column 3 up
#     7: spin row 1 right
#     8: spin row 2 right
#     9: spin row 3 right
#     10: spin row 1 left
#     11: spin row 2 left
#     12: spin row 3 left

one_four = [0,3,6]
two_five = [1,4,7]
three_six = [2,5,8]
seven_ten = [0,1,2]
eight_eleven = [3,4,5]
nine_twelve = [6,7,8]



# Checks to see if a side (iterator) is solved (all values in list are equal)

def solve_check(iterator):
	iterator = iter(iterator)
	try:
		first = next(iterator)
	except StopIteration:
		return True
	return all(first == rest for rest in iterator)


# action_index is which row or column gets affected, and action_faces is what action is
# being performed (turning up or down, left or right)

def turner(action_index,action_faces):
	for i in range(9):
		if i in action_index:
			action_faces[0] += action_faces[1][i]
			action_faces[2] += action_faces[3][i]
			action_faces[4] += action_faces[5][i]
			action_faces[6] += action_faces[7][i]
			action_faces[8] += action_faces[9][i]
			action_faces[10] += action_faces[11][i]
		else:
			action_faces[0] += action_faces[7][i]
			action_faces[2] += action_faces[1][i]
			action_faces[4] += action_faces[3][i]
			action_faces[6] += action_faces[5][i]
			action_faces[8] += action_faces[9][i]
			action_faces[10] += action_faces[11][i]



# Randomly picks one of the twelve possible ways you can turn a row or column, then does it
counter = 0
while solved == False:
	counter += 1
	print counter
	turn_picked = random.randint(1,12)
	if turn_picked == 1:
		turner(one_four,vert_down)
	elif turn_picked == 2:
		turner(two_five,vert_down)
	elif turn_picked == 3:
		turner(three_six,vert_down)
	elif turn_picked == 4:
		turner(one_four,vert_up)
	elif turn_picked == 5:
		turner(two_five,vert_up)
	elif turn_picked == 6:
		turner(three_six,vert_up)
	elif turn_picked == 7:
		turner(seven_ten,hor_right)
	elif turn_picked == 8:
		turner(eight_eleven,hor_right)
	elif turn_picked == 9:
		turner(nine_twelve,hor_right)
	elif turn_picked == 10:
		turner(seven_ten,hor_left)
	elif turn_picked == 11:
		turner(eight_eleven,hor_left)
	elif turn_picked == 12:
		turner(nine_twelve,hor_left)
	front = new_front
	right = new_right
	bottom = new_bottom
	left = new_left
	top = new_top
	back = new_back
	new_front = []
	new_left = []
	new_right = []
	new_back = []
	new_top = []
	new_bottom = []
	vert_down = [new_front, top, new_top, back, new_back, bottom, new_bottom, front,new_left,left,new_right,right]
	vert_up = [new_front, bottom, new_bottom, back, new_back, top, new_top, front,new_left,left,new_right,right]
	hor_right = [new_front, left, new_left, back, new_back, right, new_right, front,new_top,top,new_bottom,bottom]
	hor_left = [new_front, right, new_right, back, new_back, left, new_left, front,new_top,top,new_bottom,bottom]

	if counter > initial_mix:
		for i in [front,back,top,bottom,left,right]:
			if solve_check(i) == True:
				correct_sides += 1
		if correct_sides == 6:
			solved = True
		else:
			correct_sides = 0
	print counter

