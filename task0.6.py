#task 0.6
print('Enter three random numbers, the program will tell you the biggest number')
num = []
num1 = float(int(input('Enter number_1:')))
num2 = float(int(input('Enter number_2:')))
num3 = float(int(input('Enter number_3:')))
print('Your highest number is', "")
if num2<= num1>=num3:
    print(num1)
elif num1<=num2>=num3:
    print(num2)
elif num1 <= num3 >= num2:
    print(num3)