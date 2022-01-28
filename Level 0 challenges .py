x=0
y=1
print(x)
print(y)
x=x+3
y=y+x
print(x)
print(y)


x = 1+1*2
y = (1+1)*2
z = 1+(1*2)
a = 1+1*2/2
b = (1+1*2)/2
print(x)
print(y)
print(z)
print(a)
print(b)

num = int(input ('Enter a number:'))
if num%2==0:
    print(num, 'is even')
else:
    print(num, 'is odd')




name = input('Type in your name:')
print("Hello, " +  name +"!")

print('Calculating the area of a triangle, input the bread, height and base ')
bread = int(input())
height = int(input())
base = int(input())
area = (1/2* (int(bread) + int(height) + int(base) ))
print('the area is')
print(area)

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
#task 0.7
print('input the temperature in celsius to get temperature in fahrenheit')
Cel = int(input('Input temperature in celsius:'))
Fah = ((Cel * 9/5) + 32)
print('Temperature in Fahrenheit is:')
print(Fah)

#Task 0.8
Clock= float(input('Enter time to be converted to hours and minutes:'))
Hours= (Clock//60)
Minutes= Clock%60
#minute = Minutes//60
print(Hours, 'Hours', Minutes, 'Minutes')

#task 0.9
words = input('Enter any strings of words:')
#if 'A'in words or 'a' in words or 'E' in words or 'e' in words or 'O' in words or 'o'in words or 'I' in words or 'i' in words or 'U' in words or 'u' in words:
if words == 'A' or words == 'a' or words ==  'E' or words == 'e' or words == 'O' or words == 'o' or words == 'I' or words == 'i' or words ==  'U' or words == 'u':
     print('vowels in your word/s are:')
if 'a' in words:
    print('a')
if 'A' in words:
    print('A')
if 'E' in words:
    print('E')
if 'e' in words:
    print('e')
if 'O' in words:
    print('O')
if 'o' in words:
    print('o')
if 'I' in words:
    print('I')
if 'i' in words:
    print('i')
if 'U' in words:
    print('U')
if 'u' in words:
    print('u')
#task 0.10
Words = input('Enter any string of your choice: ')
Words1 = input('Enter 2nd string: ')
S1=set(Words)
s2=set(Words1)
list = S1 & s2
print(list)



