from time import time

#1. დაალაგე შემთხვევით დაგენერირებული 10 ელემენტიანი სია sort() მეთოდის გამოყენებით (ზრდადობით).
from random import randint
def randList(n):
    return [randint(1, 100) for i in range(n)]
lst = randList(10)
print(lst)
lst.sort()  
print(lst)
#2. დაალაგე შემთხვევით დაგენერირებული 10 ელემენტიანი სია sorted() ფუნქციის გამოყენებით (კლებადობით)

lst = randList(10)
print(lst)
lst = sorted(lst,reverse=True)
print(lst)

#3. from time import time
#3. დაწერე პროგრამა რომელიც შეადგენს შემთხვევით მთელ რიცხვთა სიას
# და შექმნილი სიის სორტირება სცადე ორი განსხვავებული მეთოდით (მაგ. Bubble და Selection).
# დათვალე თითოეული მეთოდისთვის სორტირებისთვის საჭირო დრო და დააკვირდი რომელი უფრო ეფექტურია
# მცირე(1000 ელემენტი), საშუალო(2000 ელემენტი) და გრძელი(3000 ელემენტი) სიის შემთხვევებში.

def bubble(list_a):
    indexing_length = len(list_a) - 1
    sorteed = False
 
    while not sorteed:
        sorteed = True
        for i in range(0, indexing_length):
            if list_a[i] > list_a[i+1]:
                sorteed = False
                list_a[i], list_a[i + 1] = list_a[i + 1], list_a[i]
    return list_a

def quick_sort(some_arr):
    arr = some_arr    
    length = len(arr)    
    if length <= 1:
        return arr    
    else:        
        pivot = arr.pop()
        items_greater = []    
        items_lower = []    
        for item in arr:
            if item > pivot:
                items_greater.append(item)        
            else:            
                items_lower.append(item)                
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

lst1000 = randList(1000)
time1 = time()
bubble(lst1000)
timebubble1000 = time() - time1

lst1000 = randList(1000)
time2 = time()
quick_sort(lst1000)
timequick1000 = time() - time2

lst2000 = randList(2000)
time3 = time()
bubble(lst2000)
timebubble2000 = time() - time3

lst2000 = randList(2000)
time4 = time()
quick_sort(lst2000)
timequick2000 = time() - time4

lst3000 = randList(3000)
time5 = time()
bubble(lst3000)
timebubble3000 = time() - time5

lst3000 = randList(3000)
time6 = time()
quick_sort(lst3000)
timequick3000 = time() - time6

print(f"""
    time on 1000 elements:
    bubble sort: {timebubble1000} seconds
    quick sort: {timequick1000} seconds
    time on 2000 elements:
    bubble sort: {timebubble2000} seconds
    quick sort: {timequick2000} seconds
    time on 3000 elements:
    bubble sort: {timebubble3000} seconds
    quick sort: {timequick3000} seconds""")
#P.S yvela daranvaze quicksortis wamebi xan mushaobs xan 0.0 ia ver gamovaswore






