# num=int(input("enter the year"))
# if(num%400==0 or num%4==0 and num%==100):
#     print("leap year")
# else:
#     print("its  not leap year")



# #to check odd or even
# num=int(input("enter the number to check:"))
# if(num%2==0):
#       print("its a even number")
# else:
#     print("its odd number")


#print even numbers from 1 to n
num=int(input("enter the last number to print"))
for num in range(1,num):
         if num%2==0:
             print("{0}".format(num))