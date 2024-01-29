#1. მომხმარებელს შემოაყვანინე ინფორმაცია და დათვალე 
#რამდენი რიცხვი, ანბანის ასო და სხვა სიმბოლოა მოცემული წინადადებაში.
#შედეგი დაბეჭდე. გამოიყენე for ციკლი, isalpha და isdigit ფუნქციები.
print("---------------task 1---------------") 
str = input("sheiyvane informacia: ")
number = 0
letter = 0
other = 0
without = 0
for char in str:
    if char.isalpha():
        letter += 1
    elif char.isdigit():
        number += 1
    else:
        if char == " ":
            other += 1
        else:
            other += 1
            without += 1
print(f"number of letters: {letter}\ndigits: {number}\nothers: {other}\nwithout spacebars: {without}")

#2.მომხმარებელს შეაყვანინე ორი წინადადება და მათგან შეადგინე მესამე შემდეგ წესებზე დაყრდნობით.
#  შექმნილი წინადადება უნდა იწყებოდეს პირველი წინადადების პირველი სიმბოლოთი,
#  რომელსაც ჯერ მოჰყვება მეორე წინადადების ბოლო სიმბოლო,
#  შემდეგ კი პირველი წინადადების მეორე სიმბოლო და მეორე წინადადების ბოლოდან მეორე სიმბოლო.
print("---------------task 2---------------")
str1 = input("sheiyvane pirveli winadadeba: ")
str2 = input("sheiyvane meore winadadeba: ")
str3 = ""
for i in range(len(str1) if len(str1)>= len(str2) else len(str2)):
    str3 += str1[i] + str2[-(i+1)]
print(str3)

#3. მომხმარებელს შეაყვანინე ორი წინადადება და შეამოწმე,
# პირველ წინადადებაში არსებული ყველა სიმბოლო თუ შედის მეორე წინადადებაში და პირიქით,
# მეორე წინადადებაში შემავალი ყველა სიმბოლო თუ შედის პირველ წინადადებაში.
# თუ ეს ორი პირობა დაკმაყოფილდა, დაბეჭდე:„Strings are balanced!“
# თუ რომელიმე პირობა დაირღვა, დაბეჭდე:„Strings are not balanced!“
print("---------------task 3---------------")
str1 = input("sheiyvane pirveli winadadeba: ")
str2 = input("sheiyvane meore winadadeba: ")
has = True
for i in range(len(str1)):
    if str1[i] not in str2:
        has = False
        break
if has:
    for i in range(len(str2)):
        if str2[i] not in str2:
            has = False
            break
    
    print(f"Strings are{' not' if not has else ''} balanced!")
else:
    print(f"Strings are{' not' if not has else ''} balanced!")
