# The happy number can be defined as a number which will yield 1 when it is replaced by the sum of
# the square of its digits repeatedly. If this process results in an endless cycle of numbers 
# containing 4, then the number is called an unhappy number

# list1=['one','two','three','four','five','six','seven','eight','nine','zero']
# list2=[1,2,3,4,5,6,7,8,9,0]
# add=0
# user=str(input("input do\n"))
# a=user.split()
# for i in a:
# 	b=list1.index(i)
# 	add=add+list2[b]
# print (add)


k=1
while k<100:
	user=str(k)
	a=[]
	sum1=0
	i=0
	while i<len(user):
		z=user[i]
		sum1=sum1+int(z)**2
		i+=1
		if i==len(user):
			if sum1==1:
				print (k, "it is happy number")
				break
			else:
				if sum1 in a:
					break
				else:
					a.append(sum1)
					user=str(sum1)
					i=0
					sum1=0
	k+=1