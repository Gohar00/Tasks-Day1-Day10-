'ex1'
# def StrMove(string, num):
##given function performs the same operation as strmove() function
#     string = string[num + 1:] + string[:num + 1]
#     return string
#
# word = input("Enter the word please: ")
# index = int(input("Enter the index please: "))
# print(StrMove(word, index))

'ex2'
##we give an initial value for sum
# sum = 0
# #Loop for all the elements of the range (0,1000)
# for i in range(1000):
#     if i % 3 == 0 or i % 5 == 0:
#         sum += i

# print(sum)

'ex3'
# def Fib(n):
## this function finds the fibonacci numbers and adds them to the newly created list
#     ml = []
##the initial 2 values are given beforehand
#     a = 0
#     b = 1
#     ml.append(a)
#     while a < n:
#         a, b = b , a + b
#         if a % 2 == 0:
#             ml.append(a)
#     return sum(ml)
#
# print(Fib(4000000))