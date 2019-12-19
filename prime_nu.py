a=int(input("nu. do"))
flag=0
while b<a:
    if a%b==0:
        flag+=1
        print (a,"is not prime")
  		break
  	b+=1
    else:
        if flag==0:
            print (a,"is a prime")

