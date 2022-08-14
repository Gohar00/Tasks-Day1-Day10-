'ex1'
# def BuildArray(target,n):
#       result = []
#       tmp = 0
#       for num in range(1, n + 1):
#           if num in target:
#               result.append('Push')
#               ans = max(len(result), tmp)
#           else:
#               result.append('Push')
#               result.append('Pop')
#       return result[:tmp]

'ex2'
# def Intersection(arr1, arr2):
##this function return an array of their intersection.
#     new_arr = []
#     #Loop for all the elements in the array
#     for i in arr1:
#         if i in arr2 and i not in new_arr:
#             new_arr.append(i)
#     return new_arr

# arr1 = [1, 2, 2, 1]
# arr2 = [2, 2]
# print(Intersection(arr1,arr2))

'ex3'

# def FindShortestSubArray(arr):
#     #left, the index of its first occurrence; and right, the index of its last occurrence
#     left, right, count = {}, {}, {}
#
#     #Loop for all the elements in the enumerated array
#     for i, x in enumerate(arr):
#         if x not in left: left[x] = i
#         right[x] = i
#         count[x] = count.get(x, 0) + 1
#
#     ans = len(arr)
#
#     #degree indicates the number of repetitions of the element
#     degree = max(count.values())
#
#     for x in count:
#         if count[x] == degree:
#             ans = min(ans, right[x] - left[x] + 1)
#
#     return ans
#
# print(FindShortestSubArray([1,2,2,3,1,4,2]))

'ex4'

# def SortArrayByParity(arr1):
##the function finds first the even numbers, then the others, and returns a new list at once
#   return ([i for i in arr1 if i % 2 == 0] + [i for i in arr1 if i % 2 != 0])
# print(SortArrayByParity([1, 2, 3, 4]))

'ex5'

# def SumOfUniqueElements(lst):
#     sum = 0
#     #Loop for all the elements in the list, and counts the number of occurrences of elements
#     for i in lst:
#         if lst.count(i) == 1:
#            sum += i
#     return sum

# print(SumOfUniqueElements([1,2,3,4,5]))

'ex6'

# def ImplementStrStr(haystack, needle):
##the function finds the second argument in the first and finds the first index
#         if len(needle) == 0:
#             res = 0
#         else:
#             for i in haystack:
#                 if needle in haystack:
#                     res = haystack.index(needle[0])
#                     break
#                 else:
#                     res = -1
#         return res

# string = "hello"
# substring = "ll"
# print(ImplementStrStr(string,substring))

'ex7'

# def LenghtofLastWord(str):
##finds the last word in the given sentence

#     #separates according to spaces
#     str = str.split()

#     return len(str[-1])

# s = "luffy is still joyboy"
# print(LenghtofLastWord(s))

'ex8'
# def Palindrom(str):
#     #makes all words lowercase
#     str = str.lower()
#     s = ""

      ##Loop for all the elements in the string,and finds the letters according to the ASCII table
#     for i in str:
#         if (ord(i) > 96 and ord(i) < 123):
#             s += i

#     if s == s[::-1]:
#         return True
#     else:
#         return False

# print(Palindrom("A man, a plan, a canal: Panama"))

'ex9'
# def UniqueEmailAddresses(emails):
##tries to find the only non-repeating one emails

#     un_em = set()
#     #Loop for all the elements in the emails and checks all conditions
#     for e in emails:
#         name, domain = e.split('@')
#         local = name.split('+')[0].replace('.', '')
#         un_em.add(local + '@' + domain)
#     return len(un_em)

# print(UniqueEmailAddresses(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))

'ex10'
# def Positions(lst, element):
#finds the starting and ending positions, and also checks beforehand if the list is empty
#     if len(lst) == 0:
#         first_pos = -1
#         last_pos = -1
#     for el in lst:
#         if el == element:
#             first_pos = lst.index(el)
#             break
#         else:
#             first_pos = -1
#     for i, el in enumerate(reversed(lst)):
#         if el == element:
#             last_pos = len(lst) - i - 1
#         else:
#             last_pos = -1
#     return first_pos,  last_pos
#
# print(Positions([],0))


