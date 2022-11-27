def slice(a):
    b=a.index("@")
    username=a[0:b]
    domain=a[b+1:]
    print("username: ",username)
    print("domain: ",domain.upper())
    
n=int(input("Number of emails:"))
p=[]

for i in range(n):
    a=input("Enter your email:").strip()
    p.append(a)
    
for j in p:
    slice(j)
