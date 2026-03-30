def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    
    if len(s)<2 or len(s)>6:
        return False
    
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    
    appear_digit=False

    for i in s:

        if not i.isdigit() and not i.isalpha():
            return False
        
        if i.isdigit() and not appear_digit:
            if int(i)==0:
                return False
            else:
                appear_digit=True

        if appear_digit and i.isalpha():
            return False
        
    return True

main()