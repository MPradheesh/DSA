def BubbleSort(numbers:list):
    for i in range(len(numbers)-1,0,-1):
        for j in range(i):
            if numbers[j]>numbers[j+1]:
                numbers[j],numbers[j+1]=numbers[j+1],numbers[j]

def Main():
    numbers:list = list(map(int,input().split()))
    BubbleSort(numbers)
    print(*numbers)
Main()