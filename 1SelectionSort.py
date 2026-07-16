"""Selection Sort Algorithm 
In this alogorithm we will find the minimum element in the list and place it at the beginning of the list and then we will find the next minimum element and place it at the second position and so on.
Time Complexity: O(n^2)
best case: O(n)"""

def SelectionSort(numbers:list):
    for i in range(len(numbers)):
        minimum:int = i
        for j in range(i+1,len(numbers)):
            if numbers[j]<numbers[minimum]:
                minimum=j
        numbers[i],numbers[minimum]=numbers[minimum],numbers[i]

def Main():
    numbers:list = list(map(int,input().split()))
    SelectionSort(numbers)
    print(*numbers)
Main()