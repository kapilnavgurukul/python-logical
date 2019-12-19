a=[12,545,16,78,45,268,85,85,21,29,13]
b=[]
c=[]
new=[]
for i in range (len(a)):
    if i%2==0:
        b.append(a[i])
    else:
        c.append(a[i])
for i in range (len(b)):
    if i<len(c):
        new.append(c[i])
    if i<len(b):
        new.append(b[i])
print (new)
    