groceries = [ ]

def add_list(addition):
	if addition.lower() in groceries:
		print "Error: this item is already on your shopping list"
		# add_list()
	else:
		groceries.append(addition) 
		groceries.sort()
		return groceries

def remove_item(R_item):
	if R_item.lower() != groceries:
		print "Error this item is not on your shopping list"
	else:
		return groceries.remove(R_item)


def main():
	answer = raw_input("Hello! Enter 1 if you want to add something to your list; Enter 2 if you want to deleate something from your list; Enter 3 if you want to see your current list")
	
	if answer == "1":
		answer2 = raw_input("Please enter the item you would like to add")
		add_list(answer2)
		main()

	elif answer == "2":
		answer3 = raw_input("Please enter item to remove")
		groceries.remove(answer3)
		main()

	else:
		print groceries
		main()


if __name__ == "__main__":
	main()
