n = int(input("Enter the value of n- "))
if(n==0):
    pass
else:
    if (n%2!=0):
        print("Weird")
    else:
        if(n>=2 and n<=5):
            print("Not Weird")
        elif(n>=6 and n<=20):
            print("Weird")
        else:
            print("Not Weird")
