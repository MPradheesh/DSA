"""Insertion Sort Algorithm
In this algorithm we will insert each element into its correct position in the sorted portion of the list.
Time Complexity: O(n^2)"""

def InsertionSort(numbers):
    for i in range(len(numbers)):
        j=i
        while (j>0 and numbers[j-1]>numbers[j]):
            numbers[j-1],numbers[j]=numbers[j],numbers[j-1]
            j-=1

def Main():
    numbers:list = list(map(int,input().split()))
    InsertionSort(numbers)
    print(*numbers)
Main()