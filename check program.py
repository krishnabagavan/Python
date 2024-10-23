# to print even  numbers from 1 to n
num=int(input("enter the last number "))
for num in range(1,num+1):
         if num%2==0:
               print("{0}".format(num))





# # assignment to check number is positive or negative
# num=int(input("enter the number"))
# if num>0:
#     print("number is positive")
# else:
#     print("num is negative")
    



# #to check profit loss
# costprice=int(input("enter the cost price"))
# sellingprice=int(input("enter the selling price"))
# if sellingprice>costprice:
#     print("profit")
# else:
#     print("loss")



# # multiplication of table
# num=int(input("enter the table name"))
# for i in range(1,11):
#     print(f"{num} X {i} ={num*i}")



# # ASSIGNMENT TO CHECK NUMBER IS DIVISIBLE BY 5 & 11
# num=int(input("enter the number"))
# if(num%5==0 and num%11==0):
#     print("yaa the number is divisible ")
# else:
#     print("no the number is not divisible")


# #python program of power of number
# num=int(input("enter the number"))
# pow=int(input("enter the power of a number"))
# total=num**pow
# print(total)




#python pogram to student grade
maths=int(input("enter the maths marks:"))
statistics=int(input("enter the statistics marks:"))
computer=int(input("enter the computer science marks:"))
per=(maths+statistics+computer)/300*100
print("your percentage is",per)
if(per>=90):
    print("grade O")
elif(per>=80):
    print("grade A")
elif(per>=70):
    print("grade B")
elif(per>=60):
    print("grade C")
else:
    print("fail")