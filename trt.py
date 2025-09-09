"""
rows=int(input("Enter the rows"))
cols=int(input("Enter the coloums"))
matrix=[]
for r in range(1,rows+1):
    elements=[]
    for c in range(1,cols+1):
        elements.append(int(input("enter the values")))
    matrix.append(elements)
print(matrix)
""
#list compression
rows=int(input("Enter the rows"))
cols=int(input("Enter the coloums"))
matrix=[[int(input("enter the values:")) for c in range(1,cols+1)] for r in range(1,rows+1)]
print(matrix)
#accessing elements from matrix
matrix=[[3,5,1],[6,5,0],[1,2,3]]
for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        print(matrix[r][c])
""
#using while looop
matrix=[[3,5,1],[6,5,0],[1,2,3]]
ind=0
while ind!=len(matrix):
    ind2=0
    while ind2!=len(matrix[0]):
        print(matrix[ind][ind2])
        ind2+=1
    ind+=1
#add diaganal matrix
matrix=[[3,5,1],[6,5,0],[1,2,3]]
res=0
for ind1 in range(len(matrix)):
    for ind2 in range(len(matrix[0])):
        if ind1==ind2:
            res+=matrix[ind1][ind2]
print(res)

#add elements to 1st coloums

matrix=[[3,5,1],[6,5,0],[1,2,3]]
res=0
for ind1 in range(len(matrix)):
    for ind2 in range(len(matrix[0])):
        if ind2==0:
            res+=matrix[ind1][ind2]
print(res)
"""

matrix1=[[3,5,1],[6,5,0],[1,2,3]]
matrix2=[[3,5,1],[5,5,0],[1,8,9]]
import numpy as np
print(np.add(matrix1,matrix2))


        

