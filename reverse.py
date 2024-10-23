#printing reverse of a number
num=int(input("please enter the number"))
reverse=0
while num>0:
    rem=num%10
    reverse=(reverse*10)+rem
    num=num//10
print(f"reverse of num{num} is {reverse}")
# Number = int(input("Please Enter any Number: "))
# Reverse = 0
# while(Number > 0):
#     Reminder = Number %10
#     Reverse = (Reverse *10) + Reminder
#     Number = Number //10

# print("\n Reverse of entered number is = %d" %Reverse)