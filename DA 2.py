# WAP to create a list of first 5 even numbers using list comprehension.

'''list1 = [i for i in range (0,10) if i%2==0]
print(list1)

# Write a Python program to Multiply every element of a list by five and assign it to a new list using list comprehension.

l1 = eval(input('enter a list: '))

l2 = [i*5 for i in l1]
print(l2)

# Write a program using list comprehension to extract and print all the numbers from a given string.

str1 = input('enter a string: ')

l1 = [i for i in str1 if i in '0123456789']
print(l1)

# Write a Python program to Matrix addition and Multiplication using list comprehension.

matrix1 = eval(input('enter a matrix: '))
matrix2 = eval(input('enter second matrix: '))
matrixAddition = []
matrixMultiplication = []
for i in range(len(matrix1)):
    matrixAddition.append([])
    matrixMultiplication.append([])

matrixSum = [matrix1[i][j] + matrix2[i][j] for i in range(len(matrix1)) for j in range(len(matrix1))]
matrixAddition[0], matrixAddition[1], matrixAddition[2] = matrixSum[0:3], matrixSum[3:6], matrixSum[6:9]

print(matrixAddition)

transposeMatrix2 = []
for i in range(0,3):
    transposeMatrix2.append([])

for i in range(0,3):
    for j in range(0,3):
        transposeMatrix2[j].append(matrix2[i][j])

sum1 = 0
matrixMultiply = []

for i in range(len(matrix1)):
    for j in range(len(matrix1)):
        for k in range(len(matrix1)):
            sum1 += matrix1[i][k]*transposeMatrix2[j][k]
        matrixMultiply.append(sum1)
        sum1 = 0

matrixMultiplication[0], matrixMultiplication[1], matrixMultiplication[2] = matrixMultiply[0:3], matrixMultiply[3:6], matrixMultiply[6:9]

print(matrixMultiplication)

# Write a Python program to create a new list of Numbers that are divisible by 7 from all the numbers in the range of 1-1000.

l1 = [i for i in range(1,1000) if i%7==0]
print(l1)

#  Find the transpose of a given matrix using list comprehension.

matrix = [[1,2,3],[4,5,6],[7,8,9]]

transpose = []
for i in range(0,3):
    transpose.append([])

for i in range(0,3):
    for j in range(0,3):
        transpose[j].append(matrix[i][j])

print(transpose)

#  Write a program to perform row wise sum and column wise sum of a matrix and store the results in two separate matrices namely row_sum and column_sum

matrix = [[1,4,0],[8,15,3],[1,9,2]]

row_sum, column_sum = 0, 0 

for i in range(0,3):
    for j in range(0,3):
        row_sum += matrix[i][j]
        column_sum += matrix[j][i]

print(row_sum, column_sum)

# Write a program to arrange all the elements in the matrix in descending order.

# Write a program to check whether two matrices are identical.

matrix1 = eval(input('enter a matrix: '))
matrix2 = eval(input('enter a second matrix: '))
isValid = True

for i in range(len(matrix1)):
    for j in range(len(matrix1)):
        if matrix1[i][j] != matrix2[i][j]:
            isValid = False
            break

if isValid == True:
    print('Both matrices are identical')
else:
    print('Matirces are not identical.')

# Write a program to get a sentence as input from the user. Using dictionary draw the histogram of characters and histogram of words in the given sentence.

sentence = input("Enter a sentence: ")

char_freq = {}

for char in sentence:
    if char not in char_freq:
        char_freq[char] = 1
    else:
        char_freq[char] += 1

print("Character Histogram:")

for char, freq in char_freq.items():
    print(char, "*" * freq)

word_freq = {}

words = sentence.split()

for word in words:
    if word not in word_freq:
        word_freq[word] = 1
    else:
        word_freq[word] += 1

print("\nWord Histogram:")

for word, freq in word_freq.items():
    print(word, "*" * freq)


# Write a Python program to find the repeated items of a tuple.

tup1 = eval(input('enter a tuple: '))

l1 = list(tup1)
l2 = []

for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i] == l1[j]:
            l2.append(l1[i])

print(l2)

# Given a Python list. Turn every item of a list into its square

list1 = eval(input('enter a list: '))

sqList = [i**2 for i in list1]
print(sqList)

# Write a program that reads a string and prints the letters in decreasing order of frequency.

str1 = input('enter a string: ')
dict1 = {}
for i in str1:
    if i not in dict1:
        dict1[i] = 1
        print(dict1)
    else:
        dict1[i] += 1

print(dict1)

# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

n = int(input('Enter the value of n: '))
dict1 = {}

for i in range(1, n+1):
    dict1[i]= i*i

print(dict1)

# Create a dictionary with the names as keys and marks as values by user input. Write a Python program to sum all the marks in a dictionary and display it.

dict1 = {'Seemant': 93, 'Shivank': 95, 'Vikram': 91}
sum1 = 0

for i in (dict1):
    sum1 += dict1[i]

print(sum1)

#  Write a Python program to create the multiplication table (from 1 to 10) of a number.

num = int(input('enter a number for multiplication table: '))

for i in range(1,11): 
    print(num, ' x ', i, ' = ', num*i)

# Find the sum of series:
  # a) 1 + 1/2 + 1/3 + ….. + 1/N.

N = int(input('enter the value of N: '))
sum1 = 0

for i in range(1, N+1):
    sum1 += 1/i

print('Sum of the series: ', sum1)
  #b) 1 + 2/4 + 3/9 + ....+ N/(N*N)

N = int(input('enter the value of N: '))
sum1 = 0

for i in range(1, N+1):
    sum1 += N/(N*N)

print('Sum of the series: ', sum1)

  #c) 1 + sqrt(2) + sqrt(3) + sqrt(4) + sqrt(N)

N = int(input('enter the value of N: '))
sum1 = 0

for i in range(1, N+1):
    sum1 += i**(1/2)

print('Sum of the series: ', sum1)

# Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for i in range(1,51):

    if i%3 == 0:
        print('Fizz')
    elif i%5 == 0:
        print('Buzz')
    elif i%15 == 0:
        print('FizzBuzz')

# Write a Python program to find numbers between 1 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be stored in a list and displayed

list1 = []

for i in range(1,401):
    y = True
    for j in str(i):
        
        if int(j)%2 != 0:
            y = False 
            break
    
    if y == True:
        list1.append(i)

print(list1)

# Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order

list1 = [10,20,30,40]
list2 = [100,200,300,400]

for i in range(len(list1)):
    print(list1[i], list2[-i-1])

# Get first, second best scores from the list.

scoresList = eval(input('enter scores in the form of list: '))
scoresList.sort(reverse=True)

scoresList1 = list(set(scoresList))
scoresList1.sort(reverse=True)

print('First and second best scores are ', scoresList1[0], ' and ', scoresList1[1])

#  Write program to display number of days in a month when the user enters the month.

monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
daysList = [31, 28, 31,30,31,30,31,31,30,31,30,31]

month = input('enter a month: ')

print(daysList[monthList.index(month)])

# Get a list of intergers from the user. Find the sum of all the elements in the even position of the list and store it in a variable called "EvenSum". Find the average of all the elements in the odd position of the list and store it in another variable called "OddAverage". Display both the values

intList = eval(input('enter a list of integers: '))
EvenSum, OddAverage = 0, 0

for i in range(0, len(intList), 2):
    EvenSum += intList[i]
for i in range(1, len(intList), 2):
    OddAverage += intList[i]

print('Sum of all elements in the even position is ', EvenSum)
print('Average of all elements in the odd position is ', OddAverage)

# Get a list of float values from the user and convert the elements to integer. Remove the duplicate values in the resultant list as well.
import math
list1 = eval(input('enter a list of float values: '))

for i in range(len(list1)):
    list1[i] = round(list1[i])

list1 = list(set(list1))

print(list1)

# Get a list of numbers from the user and sort the list in descending order of the last digit of each of the numbers in the list.

numbers = eval(input('enter numberical list: '))
list1 = []

for i in (numbers):
    list1.append(int(str(i)[::-1]))

list1.sort()
numbers = []
for i in (list1):
    numbers.append(str(i)[::-1])
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i][1] == numbers[j][1]:
            numbers.remove(numbers[j])

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
print(numbers)    

# Programming using Lists and Tuples

    #1

list1 = eval(input('enter a list of numbers: '))

def search(key):
    if key in list1:
        return (list1.index(key))
    else:
        return ('Enter a valid key')
def maximum(list1):
    list1.sort(reverse = True)
    return list1[0]
def minimum(list1):
    list1.sort()
    return list1[0]

    #2

def is_anagram(str1, str2):
    str1.strip()
    str2.strip()
    list1, list2 = list(set(list(str1.lower()))), list(set(list(str2.lower())))
    list1.sort()
    list2.sort()

    if list1 == list2:
        return True

print(is_anagram('A gentleman', 'Elegant man'))

    #3
    #4
    #5

tup  = (1,3,2,4,6,5)
l = []
for i in range(1, len(tup), 2):
    l.append(tup[i])

tup1 = tuple(l)
print(tup1)

    #6

foodList = eval(input('enter a list of food items: '))
priceList = eval(input('enter a list of prices of corresponding food items: '))
orderTup = eval(input('enter your order in form of tuple: '))

totalCost = 0

for i in range(len(orderTup)):
    totalCost += foodList[i] * priceList[i]

print('Total Amount: ', totalCost)

# Programming using Nested Lists

    #1
    #2
    #3

matrix1 = eval(input('enter a matrix: '))
matrix2 = eval(input('enter second matrix: '))
matrixAddition = []
matrixMultiplication = []
for i in range(len(matrix1)):
    matrixAddition.append([])
    matrixMultiplication.append([])

matrixSum = [matrix1[i][j] + matrix2[i][j] for i in range(len(matrix1)) for j in range(len(matrix1))]
matrixAddition[0], matrixAddition[1], matrixAddition[2] = matrixSum[0:3], matrixSum[3:6], matrixSum[6:9]

print(matrixAddition)

transposeMatrix2 = []
for i in range(0,3):
    transposeMatrix2.append([])

for i in range(0,3):
    for j in range(0,3):
        transposeMatrix2[j].append(matrix2[i][j])

sum1 = 0
matrixMultiply = []

for i in range(len(matrix1)):
    for j in range(len(matrix1)):
        for k in range(len(matrix1)):
            sum1 += matrix1[i][k]*transposeMatrix2[j][k]
        matrixMultiply.append(sum1)
        sum1 = 0

matrixMultiplication[0], matrixMultiplication[1], matrixMultiplication[2] = matrixMultiply[0:3], matrixMultiply[3:6], matrixMultiply[6:9]

print(matrixMultiplication)

# Programming using Dictionary.

    #1

N = int(input('Enter the value of n: '))
dict1 = {}

for i in range(1, N+1):
    dict1[i]= i*i

print(dict1)

    #2

FrEn={'le':'the', 'la':'the', 'livre':'book', 'pomme':'apple'}

#print(FrEn.items())

    #3

dict1 = {'A':100, 'B': 200, 'C': 300}
dict2 = {'A': 300, 'B': 500, 'D': 400}
newDict = {}

for i in dict1:
    if i in dict2:
        newDict[i] = dict1[i] + dict2[i]
    else:
        newDict[i] = dict1[i]

for i in dict2:
    if i not in dict1:
        newDict[i] = dict2[i]

print(newDict)

    #4

#scrabbleWord = input('enter a word')
pointsDict = {1: 'A,E,I,L,N,O,R,S,T,U', 2: 'D,G', 3: 'B,C,M,P', 4: 'F,H,V,W,Y', 5: 'K', 8: 'J,X', 10:'Q,Z'}

points = pointsDict.keys()

#for i in points'''
