
def sort(l):
    i = 0
    while(i< len(l)-1):
        n = l[i]
        if l[i+1] < n:
            l[i] = l[i+1]
            l[i+1] = n
            sort(l)
        i = i + 1    
    return l
 
list1 = [19,9,14,15,18,12,0,14,24,15, 2, 7, 5,45]
sort(list1)
 
print (list1)

