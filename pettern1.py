user1=int(input("no_do\n"))
z=2
while z<=user1:
	a=[]
	user=z
	for i in range (1,user+1):
		a.append(str(i))
		if i==user:
			for j in range (user-1,0,-1):
				a.append(str(j))
	a=("".join(a))
	print (a)
	z+=1