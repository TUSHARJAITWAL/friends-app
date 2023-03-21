# def reverse_arr(A,s,e):
#     while s < e:
#         A[s],A[e]=A[e],A[s]
#         s+=1
#         e-=1
# A=[1,2,3,4,5,6]
# print(A)
# reverse_arr(A , 0 , 5)
# print("Revrese array is :---",A)


a=[12,13,14,78,100,101]
s=0
e=5
while s < e:
    a[s],a[e]=a[e],a[s]
    s+=1
    e-=1
print(a)

 