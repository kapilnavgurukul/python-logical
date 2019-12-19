# a prefact number example 28=1+2+4+7+14 means some of the factors = number

user=int(input("input do"))
sum1=0
for i in range (1,user):
	if user%i==0:
		sum1+=i
if sum1==user:
	print ("perfact number")
else:
	print ("is not perfact number")

# user=input("input do")
# print (user[:2]+user[-2:])

# user=input("input do\n")
# if user[-3:]=="ing":
# 	print (user+"ly")
# elif user[-2:]=="ly":
# 	print (user)
# else:
# 	print (user+'ing')

# user=input("input do\n")
# if user[-3:]=="ing":
# 	print (user[:-3]+"ly")
# elif user[-2:]=="ly":
# 	print (user)
# else:
# 	print (user+'ing')

# user=int(input("input do\n"))
# a=0
# b=1
# c=0
# i=0
# serious=[]
# while i<user:
# 	serious.append(a)
# 	c=a+b
# 	a=b
# 	b=c
# 	i+=1
# for z in serious:
# 	if z%2==0:
# 		print (z)
# print (serious)


# user=int(input("input do\n"))
# sum1=0
# sum_sq=0
# for i in range (1,user+1):
# 	sum1+=i
# 	sum_sq+=i**2
# print (sum1**2-sum_sq)