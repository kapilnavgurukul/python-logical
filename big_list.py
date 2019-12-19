# to find a maximum number form nested list


def max_marks(list):
	for i in list:
		return max(list) 

marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
for a in marks:
	print (max_marks(a))