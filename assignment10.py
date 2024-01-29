from random import randint
import time
#1. დაწერე ფუნქცია რომელიც შეადგენს შემთხვევით მთელ რიცხვთა სიას.
def randList(n):
    return [randint(1, 100) for i in range(n)]

def timer(func):
    def wrapper(*args,**kwargs):
        t1 = time.time()
        result = func(*args,**kwargs)
        t2 = time.time() - t1
        return t2
    return wrapper

def quickSort(lst):
    arr = lst
    length = len(arr)
    if length <= 1:
        return arr
    else:
        pivot = arr.pop()
        greater = []
        lower = []
        for x in arr:
            greater.append(x) if x>pivot else lower.append(x)
    return quickSort(lower) + [pivot] + quickSort(greater)

@timer
def binary_search(arr, low, high, x):
    if high >= low:        
        mid = (high + low) // 2        
        if arr[mid] == x:
            return mid        
        elif arr[mid] > x:
            return binary_search(arr, low, mid-1, x)        
        else:            
            return binary_search(arr, mid+1, high, x)    
    else:        
        return -1

@timer
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1




lst = randList(10000)

#2. დაასორტირე შექმნილი სია რომელიმე ოპტიმალური მეთოდით.

lst = quickSort(lst)
length = len(lst)
#3. დასორტირებულ სიაში ელემენტის მოსაძებნად გამოიყენე ხაზობრივი და ბინარული ძიება.

x = binary_search(lst, 0, length-1,6000)
y = linear_search(lst,6000)
print(x)
print(y)


#4. დათვალე ძიების თითოეული მეთოდისთვის საჭირო დრო (დეკორატორის გამოყენებით) და დააკვირდი დროში სხვაობას მცირე, საშუალო და გრძელი სიის შემთხვევებში.