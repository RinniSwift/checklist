checklist = list()  # or []

# create new objects in the list
# this adds items onto the list at the back
def create(item):
	checklist.append(item)


# retrieve onjects in the list
#this reads the item in the list in that index
def read(index):
	return checklist[int(index)]


# update a list. Can only update and change items in the index of the list
# this changes the previous list to be how you choose to update it
def update(index, items):
	checklist[index] = items
	


# remove objects from the list
# this removes objects out from the list
def destroy(index):
	checklist.pop(index)

# This lists all items in the list with an index in front
def list_all_items():
	index = 0
	for list_item in checklist:
		print("{}".format(list_item))
		index += 1

def mark_completed(index):
	update(index, "{} {}".format("/", checklist[index]))



def select(function_code):

	if function_code == "C":
		input_item = input("Input item: ")
		create(input_item)

	elif function_code == "R":
		item_index = input("Input index: ")
		print(read(item_index))

	elif function_code == "P":
		list_all_items()

	elif function_code == "Q":
		return False

	else:
		print("Unknown Option")
	return True



def user_input(prompt):	
	user_input = input(prompt)
	return user_input

running = True
while running:
	selection = user_input("Press C to add to list, R to Read from list, P to display list, and Q to quit: ")
	running = select(selection)


def test():
	create("Hello World")
	create("yoooo")

	print(checklist)
	mark_completed(0)
	list_all_items()



test()

# def tests():
	# create("purple sox")
	# create("red cloak")

	# print(read(0))
	# print(read(1))

	# update(0, "purple socks")
	# destroy(1)
	# print(read(0))
	# list_all_items()

	# list_all_items()


# tests()