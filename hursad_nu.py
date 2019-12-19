
# for i in range(10,1000):
# 	i=str(i)
# 	for j in i:
# 		nu=0
# 		j=int(j)
# 		nu=nu+j
# 	i=int(i)
# 	if i % j == 0:
# 		print (i)

for i in range(10,555):
	i=str(i)
	nu=0
	for j in i:
		j=int(j)
		nu=nu+j
		i=int(i)
	if i % nu == 0:
		print (i)