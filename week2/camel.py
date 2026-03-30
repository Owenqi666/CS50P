x=input("camelCase:").strip()
result=""
for i in x:
    if i.isupper():
        result=result+"_"+i.lower()
    else:
        result=result+i
print (result)