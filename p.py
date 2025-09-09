"""#liner search 
l=[10,40,30,'a','b',70]
target=10
for ind in range(len(l)):
    if l[ind]==target:
        print(ind)
        break
else:
    print(-1)
    
#binary search--{sorted,no duplicates,homogeous}
def binary_search(l,target,least_ind,high_ind):
    while least_ind<=high_ind:
        mid_ind=(least_ind+high_ind)//2
        if l[mid_ind]>target:
            high_ind=mid_ind-1
        elif l[mid_ind]<target:
            least_ind=mid_ind+1
        elif l[mid_ind]==target:
            return mid_ind   
    return -1
l=[10,40,30,40,50,60,70,80]
target=70
least_ind=0
high_ind=len(l)
print(binary_search(l,target,least_ind,high_ind))

"""
#interpolar search {same rules but starting ind there is formula y=mx+c}


