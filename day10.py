'ex1'
# def RemoveDuplicates(arr):
#     count = 0
#     # Loop for all the elements in the array
#     for i in range(len(arr)):
#         # If the current element is equal to the next element, we skip
#         if i < len(arr) - 2 and arr[i] == arr[i + 1]:
#             continue
#         # We will update the array in place
#         arr[count] = arr[i]
#         count += 1
#     return count

# print(RemoveDuplicates([0,0,1,1,1,2,2,3,3,4]))

'ex2'
# def MergeSorted(arr1, m, arr2, n):
#
#     tmp = len(arr1) - 1
#     m = m - 1
#     n = n - 1

#     while m >= 0 and n >= 0:
#         if arr1[m] >= arr2[n]:
#             arr1[tmp] = arr1[m]
#             m -= 1
#         else:
#             arr1[tmp] = arr2[n]
#             n -= 1
#         tmp -= 1
#
#     if n >= 0:
#         arr1[:n + 1] = arr2[:n + 1]
#
#     return arr1
#
# print(MergeSorted([1,2,3,0,0,0], 3, [2,5,6], 3))

'ex3'
# def ContainsDuplicate(arr):
#     #function deletes duplicate elements
#     new_arr = set(arr)
#     return len(new_arr) != len(arr)

# print(ContainsDuplicate([1,2,3,4]))

'ex4'
# def SingleNumber(arr):
#     # Loop for all the elements in the array and check the count of elements
#     for i in arr:
#         if arr.count(i) == 1:
#             return i
# print(SingleNumber([1]))

'ex5'
# def MissingNumber(arr):
##this function find the missing number of list, the first calculate the size of array,than check
#     missing_numbers = []
#     for i in range(1,len(arr) + 1):
#         if i not in arr:
#             missing_numbers.append(i)
#     return missing_numbers
# print(MissingNumber([9,6,4,2,3,5,7,0,1]))

'ex6'
# def MaxConsecutiveOnes(arr):
##this function return the maximum number of consecutive 1's in the array
#     max_count = 0
#     tmp_count = 0

#     for i in arr:
#         if i == 1:
#             tmp_count += 1
#             if tmp_count >= max_count:
#                 max_count = tmp_count
#         else:
#             tmp_count = 0
#     return max_count

# print(MaxConsecutiveOnes([1,1,0,1,1,1]))

'ex7'

# def ArrayPartition(arr):
##first sorts then takes every second element
#     sorted_arr = arr.sort()
#     sum = 0
#     for i in range(0, len(arr), 2):
#         sum += arr[i]
#     return sum

# print(ArrayPartition([6,2,6,5,1,2]))

'ex8'

# def IsPrime(num):
##This function check is prime the number or no
#     for i in range(2,num):
#         if num % i == 0:
#             return False
#     return True

# def LargestPrimeFactor(number):
#This function find the prime numbers and added to the lst
#     lst = []
#     for i in range(2,number):
#         if number % i == 0 and IsPrime(i):
#            lst.append(i)
#     return lst[-1]

# print(LargestPrimeFactor(600851475143))

# 'ex9'????????
# from math import *
# # def solution(num):
# print(gcd(10,20))

'ex11'
# #This funtion calculate the sqr of sum
# def SqrOfSum(a,b):
#     sum_1 = 0
#     while a <= b:
#         sum_1 += a
#         a += 1
#     return sum_1 ** 2
# #This function calculate the sum of squares of numbers
# def SumOfSqr(a, b):
#     sum_2 = 0
#     while a <= b:
#         sum_2 += a**2
#         a += 1
#     return sum_2
#
# print(SqrOfSum(1,10) - SumOfSqr(1,10))

'ex12'
# def NstPrimeNumber(n):
##this 10 001st prime number
#     prime_numbers = [2]
#     attempt = 3

#     while len(prime_numbers) < n:
#         if all(attempt % prime != 0 for prime in prime_numbers):
#             prime_numbers.append(attempt)
#         attempt += 2
#     return prime_numbers[-1]

# print(NstPrimeNumber(10001))

