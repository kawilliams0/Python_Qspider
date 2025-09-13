#Quick Sort
"""def quick(l):
    if len(l)<2:
        return l
    pivot=l[0]
    left=[ele for ele in l[1:] if pivot>ele]
    right=[ele for ele in l[1:] if pivot<=ele]
    return quick(left)+[pivot]+quick(right)
l=[89,29,43,9,0,67,202,20]
print(quick(l))
#quick sort 
def quick(l):
    if len(l)<2:
        return l
    pivot =l[0]
    left=[l[ind] for ind in range(1,len(l)) if pivot>l[ind]]
    right=[l[ind] for ind in range(1,len(l)) if pivot<=l[ind]]
    return quick(left)+[pivot]+quick(right)
l=[45,56,90,7,4,23,90]
print(quick(l))"""

#String Programs
s='aba'

