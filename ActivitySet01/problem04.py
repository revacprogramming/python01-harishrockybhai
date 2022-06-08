# Conditional Execution
hrs = float(input("Enter Hours:"))
rate=float(input("enter the rate"))
if(hrs>=40):
    hrs1=hrs-40
    Pay=(40*rate)+(hrs1*1.5*rate)
    print(Pay)   
else: 
    Pay=hrs*rate
    print(Pay)

