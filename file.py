# batch1_students = ["ha pappu","or ky haal he","kaha hai","suna","9009120899","amla"]
# students_file = open("navgurukul_students.html", "w")
# students_file.write("<html> \n<tital>i_am_kapil</title>\n</head>\n<body>\n<ul>\n")
# for student in batch1_students:
# 	students_file.write("<li>"+ student +"</li>\n")
# students_file.write("</ul>\n</body>\n</html\n")
# students_file.close()


# my_file=open("people.txt","w")
# my_file.write("kapil - amla \n yogendra - chichli")
# my_file.close()
# kapil=open("people.txt","r")
# kapil_data=kapil.read()
# print (kapil_data)


# a=open("people1-exercise.txt")
# a_data=a.read()
# print (a_data)

# banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
# bank=open("file-question3.txt","w")
# for i in banks_list:
# 	bank.write(i+"\n")
# bank.close()
# kapil=open("file-question3.txt")
# kapil_data=kapil.read()
# print (kapil_data)


# a=open("people.txt","r")
# a_data=a.read()
# b=a_data.split()
# for i in b:
# 	if i=="-":
# 			b.remove("-")

# delhi=open("delhi.txt","w")
# shimla=open("shimla.txt","w")
# other=open("other.txt","w")

# j=1
# while j<len(b):
# 	if b[j]=='delhi':		
# 		delhi.write(b[j-1]+"\n")		
# 	elif b[j]=='shimla':
# 		shimla.write(b[j-1]+"\n")
# 	else:		
# 		other.write(b[j-1]+"\n")
# 	j+=2

# delhi.close()
# shimla.close()
# other.close()

# print("---------------------------delhi---------------------------")
# delhi=open('delhi.txt')
# print(delhi.read())

# print("--------------------------------shimla--------------------")
# shimla=open('shimla.txt')
# print(shimla.read())

# print("------------------------------other------------------------")
# other=open('other.txt')
# print(other.read())

print([i for i in range(29)])