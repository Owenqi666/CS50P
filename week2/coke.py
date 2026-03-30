sum=0
due=50
while due>0:
    print(f"Amount Due: {due}")
    n=int(input("Insert Coin:"))
    if n==5 or n==10 or n==25:
        due=due-n
if due<0:
    print(f"Change Owed:{-due}")