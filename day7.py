'ex1'
# def BubbleSort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr) - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
# print(BubbleSort([1,4,3,5,7,3,111]))

'ex2'

# def SelectionSort(arr):
#     for ind in range(len(arr)):
#         min_index = ind
#
#         for j in range(ind + 1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         (arr[ind], arr[min_index]) = (arr[min_index], arr[ind])
#     return arr
# print(SelectionSort([1,4,3,5,7,3,111]))

'ex3'

# def InsertionSort(arr):
#     for i in range(1, len(arr)):
#         tmp = arr[i]
#         j = i - 1
#         while (j >= 0 and tmp < arr[j]):
#             arr[j + 1] = arr[j]
#             j = j - 1
#         arr[j + 1] = tmp
#     return arr
# print(InsertionSort([1,4,3,5,7,3,111]))

'ex4'

# def MergeSort(arr):
#     if len(arr) > 1:
#         mid = len(arr)//2
#         left = arr[:mid]
#         right = arr[mid:]
#         MergeSort(left)
#         MergeSort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 arr[k] = left[i]
#                 i+=1
#             else:
#                 arr[k] = right[j]
#                 j+=1
#             k+=1
#         while i < len(left):
#             arr[k] = left[i]
#             i+=1
#             k+=1
#         while j < len(right):
#             arr[k] = right[j]
#             j+=1
#             k+=1
#
#         return arr
# print(MergeSort([1,4,3,5,7,3,111]))