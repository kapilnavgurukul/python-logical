# for calcolation

def calculator(a,b,operation):
	if operation=="+":
		return a+b
	elif operation=="-":
		return a-b
	elif operation=="*":
		return a*b
	elif operation=="/":
		return a/b
	elif operation=="%":
		return a%b
	else:
		print ("please choose the currect operator")