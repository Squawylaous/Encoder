def delta(x):
    z=x[0]
    for i in range(len(x)-1):
        if x[i]==x[i+1]: z=z+"0"
        else: z=z+"1"
    return z
def deltaeff(x):
    z=0
    for i in range(len(x)-1):
        if x[i]==x[i+1]: z+=1
    return z
def rept(x):
    x=x[1:]
    y=1
    while x[y-1]=="1": y+=1
    return y,int("1"+x[y:(y*2)],2)-1
def dedelta(x):
    y=x[0]
    for i in range(len(x)-1):
        if x[i+1]=="0": y=y+y[i]
        else: y=y+str(abs(int(y[i])-1))
    return y
yn=input("Are you encoding a number? Y/N ")
x=bin(int(input("Please input a number: ")))[2:]
xx=x
z=x
y=0
if yn=="Y" or yn=="y":
    for i in range(len(xx)-1):
        xx=delta(xx)
        if deltaeff(xx)>y:
            y=i+1
            z=x
    for i in range(y): x=delta(x)
    y=bin(y+1)[2:]
    y=("1"*(len(y)-2))+"0"+y[1:]
    print(int("1"+y+x,2),"1"+y+x)
else:
    x=x[rept(x)[0]*2+1:]
    for i in range(rept(xx)[1]): x=dedelta(x)
    print(int(x,2),x)
