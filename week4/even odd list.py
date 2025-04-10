def createlist(l,n):
    l=[]
    for i in range(n):
        temp=int(input("enter value:"))
        l.append(temp)
    return l


def esum(l):
    esum=0
    for i in range(len(l)):
        if(i%2==0):
            esum+=l[i]
    return esum
    
    
def osum(l):
    osum=0
    for i in range(len(l)):
        if(i%2!=0):
            osum+=l[i]
    return osum
    
        
l1=[]
l2=[]
l3=[]
n1=int(input("Enter limit 1: "))
n2=int(input("Enter limit 2: " ))
n3=int(input("Enter limit 3: "))
l1=createlist(l1,n1)
print(l1)
l2=createlist(l2,n2)
print(l2)
l3=createlist(l3,n3)
print(l3)

es1=esum(l1)
print("esum1=",es1)
es2=esum(l2)
print("esum2=",es2)
es3=esum(l3)
print("esum3=",es3)

os1=osum(l1)
print("osum1=",os1)
os2=osum(l2)
print("osum2=",os2)
os3=osum(l3)
print("osum3=",os3)
 
print("multipication and sumetion of esum and oddsum=",(es1+es2+es3)*(os1+os2+os3))
