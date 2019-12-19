i=35
j=0
while j<=35:
	if i+j==35 and (i*2 + j*4)==94:
		print (i,j)
		break
	i-=1
	j+=1
else:
	print ("this is wrong input")