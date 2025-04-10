Q:creat a function list 

def creatlist(l,n):
    for i in range(n):
        temp=int(input("Enter"))
        l.append(temp)
    return l


l1=[]
l2=[]
l3=[]
n1=int(input("Enter limit 1: "))
n2=int(input("Enter limit 2: "))
n3=int(input("Enter limit 3: "))
l1=creatlist(l1,n1)
print(l1)
l2=creatlist(l2,n2)
print(l2)
l3=creatlist(l3,n3)
print(l3)
