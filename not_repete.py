string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
new_list=[]
for i in string_list:
	if i not in new_list:
		new_list.append(i)
print (new_list)