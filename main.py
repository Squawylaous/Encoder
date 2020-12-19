def delta(x):
    z=x[0]
    for i in range(len(x)-1):
        if x[i]==x[i+1]: z=z+"0"
        else: z=z+"1"
    return z
def deltaeff(x,ii):
    y=0
    yy=0
    yyy=0
    z=0
    zz=0
    zzz=0
    x=numshort(ii)+x
    for i in range(len(x)-1):
        if x[i]=="0" and x[i+1]=="0": y+=1
        elif y!=0: yy+=len(numshort(y))-(y+1)
        if x[i]=="1" and x[i+1]=="1": z+=1
        elif z!=0: zz+=len(numshort(z))-(z-1)
        if x[i]=="0": yyy+=1
        if x[i]=="1": zzz+=1
    yyy+=yy
    zzz+=zz
    if zzz>yyy: yyy=zzz
    return yyy
def rept(x):
    y=1
    while x[y-1]=="1": y+=1
    return x[y*2:],int("1"+x[y:(y*2)],2)-1
def dedelta(x):
    y=x[0]
    for i in range(len(x)-1):
        if x[i+1]=="0": y=y+y[i]
        else: y=y+str(abs(int(y[i])-1))
    return y
def numshort(x):
    x=bin(x+1)[2:]
    x=("1"*(len(x)-2))+"0"+x[1:]
    return x
def rle(x):
    y=0
    z=0
    v=0
    for i in range(len(x)):
        if x[i]=="0": y+=1
        if x[i]=="1": z+=1
    if y>z: ww="0"
    else: ww="1"
    w="1"+ww+x[len(x)-1]
    for i in range(len(x)):
        if x[i]==ww:
            v+=1
            d=True
        else:
            w=w+numshort(v+1)
            v=0
            d=False
    if d:
        w=w+numshort(v+1)
        v=0
    return w
def derle(x):
    if x[1]=="0": z="1"
    else: z="0"
    w=x[1]
    d=x[2]
    x=x[3:]
    y=w*(rept(x)[1]-1)
    x=rept(x)[0]
    while x!="":
        y=y+z+(w*(rept(x)[1]-1))
        x=rept(x)[0]
    if d!=w: y=y+d
    return y
def encode(x):
    y=0
    xx=x
    for i in range(len(xx)):
        xx=delta(xx)
        if deltaeff(xx,i+1)>y: y=i+1
    for i in range(y): x=delta(x)
    x=rle(numshort(y+1)+x)
    return hex(int(x,2))[2:]
def decode(x):
    x=derle(x)
    xx=x
    x=rept(x)[0]
    for i in range(rept(xx)[1]-1): x=dedelta(x)
    return hex(int(x,2))[2:]
def percreduc(x,xx):
    if x<xx: x=(x/xx)*100
    else: (xx/x)*-100
    return round(x,2)
yn=input("Are you encoding a number? Y/N ")
x=bin(int(input("Please input a number: "),16))[2:]
if yn=="Y" or yn=="y": xx=encode(x)
else: xx=decode(x)
if yn=="Y" or yn=="y": perc="\n"+str(percreduc(len(x),len(xx)))+"%"
else: perc=""
print(xx,perc)
