x=input("Expression:")
a, b, c = x.split(" ")
a=int(a)
c=int(c)
if b=="+":
    print(f"{(a+c):.1f}")
elif b=="-":
    print(f"{(a-c):.1f}")
elif b=="*":
    print(f"{(a*c):.1f}")
else:
    print(f"{(a/c):.1f}")