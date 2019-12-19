list1=[5,65,75,2,11,2,11,2,65,2,75,2,1,4,75,2,656,4,65,65,11,211,211,21]
new_list=[]
new_list1=[]
for i in list1:
	if i not in new_list:
		new_list.append(i)
	else:
		if i not in new_list1:
			new_list1.append(i)
print (new_list1)
