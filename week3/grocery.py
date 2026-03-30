a = {}
while True:
    try:
        x=input("").upper()
        if x in a:
            a[x]=a[x]+1
        else:
            a[x]=1
    except EOFError:
        print("")
        break
for i in sorted(a):
    print(a[i],i)
