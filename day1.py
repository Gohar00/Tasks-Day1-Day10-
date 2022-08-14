'ex1'
# #open the file
# with open('file.txt') as f:
#     elements = f.read()
# sum = 0
# #Loop for all the elements in the array and check if element is digit then added to the sum
# for elem in elements:
#     if elem.isdigit():
#         sum += int(elem)
# print(sum)

'ex2'
# #open both files
# with open('file1.txt', 'r') as first_file, open('file2.txt', 'a') as second_file:
#     # read content from first file
#     for line in first_file:
#         # append content to second file
#         second_file.write(line.title())

'ex3'
# #function that counts the number of elements and adds them to the dictionary
# def CountOfItems(ml):
#     my_dict = {}
#     #Loop for all the elements in the array
#     for i in my_list:
#         if i in my_dict:
#             my_dict[i] += 1
#         else:
#             my_dict[i] = 1
#     #Loop for all the elements in the dictionary`s items
#     for key, value in my_dict.items():
#         print("%d : %d" % (key,value))
#
# my_list = [1, 2, 4, 5, 7, 9, 3, 5, 67, 3]
# #function call
# CountOfItems(my_list)

'ex4'

# symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '?', '>', '<', '.']
# #giv an inital value for count of symbols
# count_of_symbols = 0
# #open the file
# with open('file1.txt') as f:
#     elements = f.read()
#     #Loop for all the elements in the array, if element is symbol than the count increases by one
#     for i in elements:
#         if i in symbols:
#             count_of_symbols += 1
#     print(count_of_symbols)

'ex5'

# def NewString(my_str):
# #The function, which will remove every third character of the received string.
#
#     new_str = ''
#     #Loop for all the elements in the array
#     for i in range(len(my_str)):
#         if i % 3 != 0:
#             new_str += my_str[i]
#         else:
#             continue
#     return new_str
#
# #requires the string to be imported
# my_str = input("Enter your text please: ")
# #call of function
# print(NewString(my_str))


'ex6'
##similar to the third exercice
# def CountOfWords(ml):
#     my_dict = {}
#     for i in my_list:
#         if i in my_dict:
#             my_dict[i] += 1
#         else:
#             my_dict[i] = 1
#
#     for key, value in my_dict.items():
#         print(f'{key} : {value}')
#
# with open('file2.txt') as f:
#     txt = f.read()
# my_list = txt.split(' ')
# CountOfWords(my_list)


'ex7'
# def SqrOfNumbers(ml):
#     return sorted([i**2 for i in ml])

# my_list = [2, 5, 6, 1, 4]
# print(SqrOfNumbers(my_list))

'ex8'
##In this problem, I count the remainder of the number,add it to the sum, and reduce the number
# def SumOfNumbers(num):
#     sum = 0
#     while (num != 0):
#         sum = sum + num % 10
#         num = num // 10
#     return sum

# number = int(input("Please enter your number: "))
# print(SumOfNumbers(number))

'ex9'
# def DivOfNumber(num):
#     sum = 0
#     mul = 1
#     while num != 0:
#         sum = sum + num % 10
#         mul = mul * (num % 10)
#         num = num // 10
#     return mul - sum

# number = int(input("Please enter your number: "))
# print(DivOfNumber(number))

'ex10'
# def Count(start, end):
##this function gets the start and end of the range
#     #is a preliminary check, if the specified interval is wrong, then it changes it by places
#     count = 0
#     if start > end:
#        tmp = start
#        start = end
#        end = tmp
#
#     #Loop for all the elements in the array, if the number is not divisible by 2, then it is odd
#     for i in range(start, end + 1):
#         if i % 2 != 0:
#             count += 1
#             print(i)
#     return count
#
# num_1 = int(input('Please enter first number: '))
# num_2 = int(input('Please enter second number: '))
# print(f'count is: {Count(num_1, num_2)}')

