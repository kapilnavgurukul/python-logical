# a=int(input("ak number dalo"))
# i=1
# while i<=a:
# 	if i%3==0 or i%5==0:
# 		print (i)
# 	i+=1



a=int(input('year dalo'))
if a%4==0:
	if a%100==0:
		if a%400==0:
			print (a, "leap year hai")
		else:
			print (a, "leap year nahi hai")
	else:
		print (a, "leap year hai")
else:
	print (a, "leap year nahi hai")




# user=int(input("input do"))
# i=user-1
# flag=0
# pichle_even=[]
# agle_odd=[]
# while i<user:
# 	if i%2==0:
# 		pichle_even.append(i)
# 		flag+=1
# 	if flag==3:
# 		j=user+1
# 		flag1=0
# 		while j>user:
# 			if j%2!=0:
# 				agle_odd.append(j)
# 				flag1+=1
# 			if flag1==3:
# 				break
# 			j+=1
# 	if flag==3:
# 		break
# 	i-=1
# print ("pichle_even : ",pichle_even)
# print ("agle_odd :" ,agle_odd)




# user=int(input("year dalo"))
# pichhle=[]
# aagle=[]
# i=user-1
# flag=0
# while i<user:
# 	if i%4==0:
# 		if i%100==0:
# 			if i%400==0:
# 				pichhle.append(i)
# 				flag+=1
# 		pichhle.append(i)
# 		flag+=1
# 	if flag==3:
# 		flag1=0
# 		j=user+1
# 		while j>user:
# 			if j%4==0:
# 				if j%100==0:
# 					if j%400==0:
# 						aagle.append(j)
# 						flag1+=1
# 				aagle.append(j)
# 				flag1+=1
# 			if flag1==3:
# 				break
# 			j+=1
# 	if flag==3:
# 		break
# 	i-=1
# print ("pichhle : ",pichhle)
# print ("aagle : ",aagle)



# user=int(input("number do"))
# b=str(user)
# z=1
# while z<=user:
# 	sum=0
# 	for i in str(z):
# 		a=int(i)**3
# 		sum+=a
# 	if sum==z:
# 		print (z)
# 	z+=1





# user=int(input("input do"))
# for i in range(2,user):
# 	sum=0
# 	for j in range(1,i):
# 		if i%j==0:
# 			sum+=j
# 	if sum==i:
# 		print (i)



# a=str(input("pahla do"))
# b=str(input("dusra do"))
# flag=0
# if len(a)==len(b):
# 	for i in a:
# 		if i not in b:
# 			flag+=1
# 	for j in b:
# 		if j not in a:
# 			flag+=1
# 	if flag==0:
# 		print ("hai")
# 	else:
# 		print ("nahi hai")
# else:
# 	print ("nahi hai")

