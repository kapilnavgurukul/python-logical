# a="aMan JHa"
# b=""
# for i in a:
# 	if ord(i) in range(65,97):
# 		b+=chr(ord(i)+32)
# 	elif ord(i) in range (97,123):
# 		b+=chr(ord(i)-32)
# 	else:
# 		b+=i          
# print (b)



# a=[[5,8,9,10,88],[5,8,7,84,2,11],[65,87,44,85,5]]
# b=[]
# for i in a:
# 	b.append(max(i))
# print (b)
# print (max(b))


# a=int(input("give input"))
# ans=1
# for i in range (1,a+1):
# 	ans*=i
# print (ans)


# a=1
# while a>0:
# 	flag=True
# 	for i in range (1,11):
# 		if a%i==0:
# 			continue
# 		else:
# 			flag=False
# 			break
# 	print(a)
# 	if flag==True:
# 		print (a)
# 		break
# 	else:
# 		a+=1


# user=int(input("give input"))
# flag=True
# for i in range (2,user):
# 	if user%i==0:
# 		flag=False
# 	else:
# 		continue
# if flag:
# 	print ("this is a prime number",user)
# else:
# 	print ("this is not a prime number")


# a=[2,55,2,11,4,74,14,25,14,87,36,54,78,14,24,85,78,45,1]
# not_in_a=[]
# max_=max(a)
# min_=min(a)
# for i in range (min_,max_):
# 	if i not in a:
# 		not_in_a.append(i)
# print (not_in_a)


# students=[]
# number=[]
# main_list=[]
# for i in range(int(input())):
#     name = input()
#     score = float(input())
#     number.append(score)
#     students.append([name,score])
# min1=min(number)
# number1=[]
# a=0
# for i in number:
#     if i==min1:
#         pass
#     else:
#         number.append(i)


# min2=min(number1)
# for i in students:
#     if i[1]==min2:
#         main_list.append(i[0])
# b=sorted(main_list)
# for i in b:
#     print (i)
