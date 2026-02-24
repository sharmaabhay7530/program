#program to calculate profit or loss based on cost price and selling proce
#input of the cost price
cp = float(input("enter cost price(in Rs): "))
# to validate cost price 
if(cp <=0):
    print("Invalid cost price")
    exit() #exiting the program if cost price is invalid
else:
    #input of selling price
    sp = float(input("enter selling price(in rs):"))
    #to validate selling price
    if(sp<=0):
        print("invalid selling price")
        exit()
    else:
        if(sp>cp):
        print("profit: Rs",(sp-cp))
        elif(cp>sp):
            print("loss: Rs",(cp-sp))
            else:
                print("no profit no loss")
                