# Part A
# WAP to add two number and print the result
'''num1 = int(input('Enter the first number to add: '))
num2 = int(input('Enter the second number to add: '))
print('Sum:', num1 + num2)

# WAP to find the area of the triangle
side1 = int(input('Enter the length of the first side: '))
side2 = int(input('Enter the length of the second side: '))
side3 = int(input('Enter the length of the third side: '))
semiPerimeter = (side1 + side2 + side3) / 2
areaOfTriangle = pow((semiPerimeter * (semiPerimeter - side1)
                     * (semiPerimeter - side2) * (semiPerimeter - side3)), 0.5)
print('Area of Triangle', areaOfTriangle)

# WAP to find the square root of a number
number = int(input('Enter the number whose square root to be found: '))
print('Square Root', number ** 0.5)

# WAP to solve the square root of a equation
print('ax^2 + bx + c')
a, b, c = int(input('Enter value of a: ')), int(
    input('Enter value of b: ')), int(input('Enter the value of c: '))
print('Factors of the equation {}x^2 + {}x + {} are'.format(a, b, c), (-b + ((b **
      2) - 4 * a * c) ** 0.5) / (2 * a), (-b - ((b ** 2) - 4 * a * c) ** 0.5) / (2 * a))

# WAP to convert Farhenheit and Celsius
farhenheit = int(input('Enter temperature in farhenheit: '))
print((farhenheit - 32) * 5 / 9)

# WAP to print the quotient and reminder after division
dividend, divisor = int(input('Enter the dividend: ')
                        ), int(input('Enter the divisor: '))
print('The quotient and remainder for the numbers {} and {} is {} and {} respectivly'.format(
    dividend, divisor, dividend // divisor, dividend % divisor))

# WAP to swap two numbers using tuple assignment
tupleOriginal = eval(input('Enter a tuple of length 2: '))
swapedTuple = (tupleOriginal[1], tupleOriginal[0])
print('Original Values {} \nSwaped Values: {}'.format(tupleOriginal, swapedTuple))

# WAP to find the average of three marks
mark1, mark2, mark3 = int(input('Enter 1st mark: ')), int(
    input('Enter 2nd mark: ')), int(input('Enter 3ed mark:'))
print((mark1 + mark2 + mark3) / 3)

# WAP to print Simple Interest
principleAmount, interestRate, timePeriod = int(input('Enter Principle Amount: ')), int(
    input('Enter interest rate: ')), int(input('Enter time period: '))
print('Interest Amount:', principleAmount * interestRate * timePeriod / 100)

# Write a program in python to calculate the net pay given basic pay, hra, da and deductions. 


# Part B
# Given age determine whether a person is eligible to vote or not. (if else) 
ageOfPerson = int(input('Enter the age of the person to check eligiblity: '))
if ageOfPerson >= 18:
    print(True)
else:
    print(False)

# Check whether a number is odd or even. (if else)
enteredNumber = int(input('Enter the number to check if even ot odd: '))
if enteredNumber % 2 == 0:
    print('Even')
else:
    print('Odd')

# Write a program to find largest of two numbers. (if else)
num1, num2 = int(input('Enter first number: ')), int(input('Enter second number: '))
if num1 > num2 :
    print('the first number entred {} is greater then the second number entered {}'.format(num1, num2))
else:
        print('the first number entred {} is lesser then the second number entered {}'.format(num1, num2))

# Obtain a character convert lower case to uppercase and vice versa. (if else)
print(input('Enter a charcater to toggle case: ').swapcase())

# Find the input year is leap year or not. (if else)
yearEntered = int(input('Enter the year to check if it\'s a leap year: '))
if yearEntered % 100 == 0:
    if yearEntered % 400 == 0:
        print('Leap Year')
    else:
        print('Not a Leap Year')
elif yearEntered % 4 == 0:
    print('Leap Year')
else: 
    print('Not a Leap Year')

# Read a number, check if it is positive, negative or zero. Increment the number if it is positive, decrement if it is negative. (elif statement)
numEntered = int(input('Enter a number: '))
if numEntered == 0:
    print('The number entered is ZERO')
elif numEntered > 0:
    print('The number entered is positive and its value after increment is',numEntered + 1)
else:
        print('The number entered is negative and its value after decrement is',numEntered - 1)

# Create a simple calculator. (elif statement)
while(True):
    print('---------------- Welcome User ---------------')
    print(''''''1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
0. Exit
Please Select A Option to Perform An Operation'''''')
    ch = int(input('Enter Your Choice: '))
    if ch == 1:
        x = int(input('Enter a Number: '))
        y = int(input('Enter a Number: '))
        print(x, '+' ,y , '=', x + y)
        print()
    elif ch == 2:
        x = int(input('Enter a Number: '))
        y = int(input('Enter a Number: '))
        print(x, '-' ,y , '=', x - y)
        print()
    elif ch == 3:
        x = int(input('Enter a Number: '))
        y = int(input('Enter a Number: '))
        print(x, '*' ,y , '=', x * y)
        print()
    elif ch == 4:
        x = int(input('Enter a Number: '))
        y = int(input('Enter a Number: '))
        print(x, '/' ,y , '=', x / y)
        print()
    elif ch == 0:
        print('Exiting.....')
        print()
        break
    else:
        print('Wrong Option! Option Doesn\'t Exist. Please Select A Suitable Option.')
        print()

# Estimate the Grade based on the marks obtained by a student. (elif statement)
markEntered = int(input('Enter Marks: '))
if 91 <= markEntered <= 100:
    print('A Grade')
elif 81 <= markEntered < 91:
    print('B Grade')
elif 71 <= markEntered < 81:
    print('C Grade')
elif 61 <= markEntered < 71:
    print('D Grade')
elif 51 <= markEntered < 61:
    print('E Grade')
else:
    print('F Fail')

# Find the largest of 3 numbers. (elif statement)
num1, num2, num3 = int(input('Enter first number: ')), int(input('Enter second number: ')), int(input('Enter third number: '))
if num1 > num2 and num1 > num3:
    print(num1, 'is the greatest')
elif num2 > num1 and num2 > num3:
    print(num2, 'is the greatest')
else:
    print(num3, 'is the greatest')

# Obtain a character, check if it is lower case, uppercase or digit. (elif statement)
character = input('Enter a charaacter: ')
if character.isalpha():
    if character.islower():
        print('The entered character is an alphabet and in lower case')
    elif character.isupper():
        print('The entered charecter is an alphabet and in upper case')
elif character.isdigit():
    print('The entered number is numeric')
else:
    print('The entered number is neither an alphabet nor number')


# Part C
# Write a program to check whether a number is odd or even.
enteredNumber = int(input('Enter the number to check if even ot odd: '))
if enteredNumber % 2 == 0:
    print('Even')
else:
    print('Odd')

# Write a program in python to find the biggest of two numbers.
num1, num2 = int(input('Enter first number: ')), int(input('Enter second number: '))
if num1 > num2 :
    print('the first number entred {} is greater then the second number entered {}'.format(num1, num2))
else:
        print('the first number entred {} is lesser then the second number entered {}'.format(num1, num2))

# Write a program to convert a character from lower case to uppercase and vice versa.
print(input('Enter a charcater to toggle case: ').swapcase())

# Write a program in python to find whether a number is divisible by both 5 and 7.
num = int(input('Enter a number: '))
while 10 <= num <= 99:
    if num % 5 == 0 and num % 7 != 0:
        print(num, 'Divisible by 5')
    elif num % 7 == 0 and num % 5 != 0:
        print(num, 'Divisible by 7')
    elif num % 35 == 0:
        print(num, 'Divisible by 5 and 7')
    num += 1

# Write a program to find the input year is leap year or not.
yearEntered = int(input('Enter the year to check if it\'s a leap year: '))
if yearEntered % 100 == 0:
    if yearEntered % 400 == 0:
        print('Leap Year')
    else:
        print('Not a Leap Year')
elif yearEntered % 4 == 0:
    print('Leap Year')
else: 
    print('Not a Leap Year')

# Write a program in python to input three sides of a triangle and check whether the triangle is equilateral, isosceles or scalene
side1 = int(input('Enter the length of the first side: '))
side2 = int(input('Enter the length of the second side: '))
side3 = int(input('Enter the length of the third side: '))
if side1 == side2 and side2 == side3:
    print('Equilateral Triangle')
elif (side1 == side2) or (side1 == side3) or (side3 == side2):
    print('Isosceles Triangle')
else:
    print('Scalene Triangle')

# Write a program in python to input three sides of a triangle and check whether it is right angled one.
side1 = int(input('Enter the length of the first side: '))
side2 = int(input('Enter the length of the second side: '))
side3 = int(input('Enter the length of the third side: '))
if side1 ** 2 == side2 ** 2 + side3 ** 2 or side2 ** 2 == side1 ** 2 + side3 ** 2 or side3 ** 2 == side1 ** 2 + side2 ** 2:
    print('The triangle is a right angle triangle')
else:
    print('The triangle isn\'t a right angle triangle')

# Read a number, check if it is positive, negative or zero. Increment the number if it is positive, decrement if it is negative.
numEntered = int(input('Enter a number: '))
if numEntered == 0:
    print('The number entered is ZERO')
elif numEntered > 0:
    print('The number entered is positive and its value after increment is',numEntered + 1)
else:
        print('The number entered is negative and its value after decrement is',numEntered - 1)

# Create a simple calculator.
while(True):
    print('---------------- Welcome User ---------------')
    print(''''''1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
0. Exit
Please Select A Option to Perform An Operation'''''')
    ch = int(input('Enter Your Choice: '))
    if ch == 1:
        x = int(input('Enter a Number: '))
        y = int(input('Enter a Number: '))
        print(x, '+' ,y , '=', x + y)
        print()
    elif ch == 2:
        x = int(input('Enter a Number: '))
        y = int(input('Enter a Number: '))
        print(x, '-' ,y , '=', x - y)
        print()
    elif ch == 3:
        x = int(input('Enter a Number: '))
        y = int(input('Enter a Number: '))
        print(x, '*' ,y , '=', x * y)
        print()
    elif ch == 4:
        x = int(input('Enter a Number: '))
        y = int(input('Enter a Number: '))
        print(x, '/' ,y , '=', x / y)
        print()
    elif ch == 0:
        print('Exiting.....')
        print()
        break
    else:
        print('Wrong Option! Option Doesn\'t Exist. Please Select A Suitable Option.')
        print()

# Estimate the Grade based on the marks obtained by a student.
markEntered = int(input('Enter Marks: '))
if 91 <= markEntered <= 100:
    print('A Grade')
elif 81 <= markEntered < 91:
    print('B Grade')
elif 71 <= markEntered < 81:
    print('C Grade')
elif 61 <= markEntered < 71:
    print('D Grade')
elif 51 <= markEntered < 61:
    print('E Grade')
else:
    print('F Fail')

# Obtain a character, check if it is lower case, uppercase or digit.
character = input('Enter a charaacter: ')
if character.isalpha():
    if character.islower():
        print('The entered character is an alphabet and in lower case')
    elif character.isupper():
        print('The entered charecter is an alphabet and in upper case')
elif character.isdigit():
    print('The entered number is numeric')
else:
    print('The entered number is neither an alphabet nor number')

# Find the largest of 3 numbers.
num1, num2, num3 = int(input('Enter first number: ')), int(input('Enter second number: ')), int(input('Enter third number: '))
if num1 > num2 and num1 > num3:
    print(num1, 'is the greatest')
elif num2 > num1 and num2 > num3:
    print(num2, 'is the greatest')
else:
    print(num3, 'is the greatest')

# Obtain a input from the user and display the corresponding data types (primitive and compound data type)



# Part D
# Compute Exponentiation (power of a number) without using ** operator.
number = int(input('Enter a number: '))
square = 1
i = 1
while i <= 2:
    square *= number
    i += 1
print(square)

# Write a program in python to print all the two digit numbers which are either divisible by 3 or by 4.
num = 10
while 10 <= num <= 99:
    if num % 3 == 0 and num % 4 != 0:
        print(num, 'Divisible by 3')
    elif num % 4 == 0 and num % 3 != 0:
        print(num, 'Divisible by 4')
    elif num % 12 == 0:
        print(num, 'Divisible by 3 and 4')
    num += 1

# Write a program in python to print the sum of all the digits of a number.
number = input('Enter a number: ')
rangeOfLoop = 0
sum  = 0
while rangeOfLoop < len(number):
    sum += int(number[rangeOfLoop])
    rangeOfLoop += 1
print(sum)

# Perform the division operation and find the quotient and remainder values. (without using /, // % operators)
dividend, divisor = int(input('Enter dividend: ')), int(input('Enter divisor: '))
remainder, quotient = 0, 0
while True:
    remainder = dividend - divisor 
    quotient += 1
    dividend = remainder
    if remainder < divisor:
        break
print(remainder, quotient)

# Check whether the given number is palindrome or not
number = int(input('Enter a number: '))
if number == int(str(number)[::-1]):
    print('Pallendrome')

# Check whether the given number is Armstrong number or not
x = int(input('Enter a number to check if its an armstrong number: '))
y = list(str(x))
c = 0
i = 0
while i < len(y):
    c += int(y[i])**len(y)
    i += 1
if x == c:
    print('The Entered Number is an Armstrong Number')
else:
    print('The Entered Number is Not an Armstrong Number')'''

# Compute the GCD of two numbers.(Euclidean Method and using common factors)
num1, num2 = int(input('Entter first number: ')), int(input('Entter second number: '))
while True:
    remainder = num1 % num2
    if remainder == 0:
        print('The GCD is',num2)
        break
    else:
        num1 = num2
        num2 = remainder

# # Take integer inputs from user until he/she presses q (Ask to press q to quit after every integer input ). Print average and product of all numbers.
prodOfVal, listOfVal = 1, []
while True:
    num = int(input('Enter the number: '))
    listOfVal.append(num)
    prodOfVal *= num
    ch = input('Do you want to quit: ')
    if ch.lower() == 'q':
        break
print('The product of the values entered is', prodOfVal)
print('The average of the values entered is', sum(listOfVal) / len(listOfVal))

# Find the square root of a number. (Newton’s method) 
num = int(input('Enter the number whose square root to be found: '))
precision = 10 ** (-10)
r = num
while abs(num - r * r) > precision:
        r = (r + num / r) / 2
print(r)


# Part E
# Write a Python program to construct the following pattern, using a nested for loop.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * * 
# *
# a)
numberOfRows = int(input('Enter the maximum number of elemets in a row: '))
topHalf = ['* ' * i for i in range(1, numberOfRows + 1)]
for i in topHalf:
    print(i)
for j in topHalf[:len(topHalf) - 1][::-1]:
    print(j)

# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
# b)
numberOfRows = int(input('Enter the number of rows: '))
for i in range(1, numberOfRows + 1):
    for j in range(i , 0, -1):
        print(j, end = ' ')
    print()

#     1 
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1
#1 5 10 10 5 1
# 2. Write a Python program that accepts a word from the user and reverse it.
from math import factorial
n = int(input('Enter the number of rows: '))
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    print()


# 3. Write a Python program to count the number of even and odd numbers from a series of numbers.
listEntered = eval(input('Enter a list: '))
print('Even Values:', [i for i in listEntered if i % 2 == 0])
print('Odd Values:', [i for i in listEntered if i % 2 != 0])

# 4. Write a Python program that prints each item and its corresponding type from the following list.
listEntered = eval(input('Enter a list: '))
for i in listEntered:
    print(i,type(i))

# 5. Write a Python program that prints all the numbers from 0 to 6 except 3 and
for i in range(0,6):
    if i != 3:
        print(i)

# 6. Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for i in range(1,51):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# 7. Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.
listWithEvenNumbers = []
for i in range(1,401):
    if [0 for j in str(i) if int(j) % 2 == 0] == [0] * len(str(i)): listWithEvenNumbers.append(i)
print('Values:', ' '.join([str(i) for i in listWithEvenNumbers]))

# 8. Write a Python program to create the multiplication table (from 1 to 10) of number.
numberWhoseMultiplication = int(input('Enter the number of the multiplication: '))
for i in range(1,11):
    print(numberWhoseMultiplication, 'x', i, '=', numberWhoseMultiplication * i)

# 9. Find the sum of series:
# a. 1 + 1/2 + 1/3 + ….. + 1/N
# b. 1 + x^2/2 + x^3/3 + … x^n/n
# a)
# a)
numberOfTerms = int(input('Enter the number of the terms: '))
sumOfTerms = 0
for i in range(1,numberOfTerms + 1):
    sumOfTerms += 1 / i

# b)
numberOfTerms = int(input('Enter the number of the terms: '))
x = int(input('Enter value of x'))
sumOfTerms = 1
for i in range(2,numberOfTerms + 1):
    sumOfTerms += (x ** i) / i

# 10. Classify the given number is prime or composite number. 
number = int(input('Enter a number: '))
count = 0
for i in range(2, number / 2):
    if number % i == 0:
        count += 1
if count == 0:
    print('Prime')
else:
    print('Composite')