# An integer number in base 10 which is divisible by sum of it digits is said to be a Harshad Number.
#  An n-harshad number is an integer number divisible by sum of its digit in base n.
# Below are first few Harshad Numbers represented in base 10:
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 20………



def is_harshad_number(a):
	b=list(str(a))
	sum=0
	for i in b:
		c=int(i)
		sum=sum+c
	if a%sum==0:
		return True
	else:
		return False
print (is_harshad_number(65))


z=1
while z<1000:
	is_harshad_number(z)
	if is_harshad_number(z)==True:
		print (z)
	z+=1



