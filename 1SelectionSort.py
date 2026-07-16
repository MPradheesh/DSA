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