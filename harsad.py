# def harsad_nu(a):
# 	for b in range (1,a+1)
# 		b=list(str(a))
# 		count=0
# 		for i in b:
# 			z=int(i)
# 			count=count+z
# 		if a%count==0:
# 			print ("harsad_nu hai")
# harsad_nu(89)

for i in range (10,1001):
	i=list(str(i))
	num=0
	for j in i:
		num=num+int(j)
	if int(i)%num==0:
		print (num)