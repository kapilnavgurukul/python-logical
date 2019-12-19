# user=str(input("sentence do"))
# a=user.split()
# print (len(a))


dics={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
user=str(input("sentence do\n"))
a=user.split()
sum1=0
for i in a:
	sum1+=dics[i]
print (sum1)