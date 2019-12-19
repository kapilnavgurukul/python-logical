`# def prime(a):
# 	for i in range (2,a):
# 		if a%i==0:
# 			return False
# 	else:
# 		return True

# user=int(input("input do"))
# a=2
# count=0
# while a>0:
# 	z=(prime(a))
# 	if z==True:
# 		count+=1
# 	if user==count:
# 		print (a)
# 		break
# 	a+=1

user=int(input("input do"))
def prime(user):
	for i in range (2,user):
		if user%i==0:
			return False
			break
	else:
		return True
z=0
a=2
while a>0:
	if prime(a):
		z+=1
	if z==user:
		print(a)
		break
	a+=1
