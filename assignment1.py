#1. დაწერეპროგრამა რომელიც გეკითხება ჯერ სახელს, შემდეგ გვარს და ინფორმაციის მიღების შემდეგ ტერმინალში ბეჭდავს ერთმანეთის გვერდით. 
print("1st task:")
name = input("Enter your name:")
surname = input("Enter your surname:")
print(name +" "+ surname)

#2. დაწერე პროგრამა რომელიც ითხოვს ორ რიცხვს, პირველი რიცხვი აჰყავს მეორის ხარისხში და შედეგი იბეჭდება ტერმინალში.
print("2nd task:")
num = input("Enter number:")
pow = input("Enter power:")
print(int(num)**int(pow))

#3. დაწერე პროგრამა რომელიც გეკითხება სახელს, გვარს, ასაკს და ქალაქს და ბეჭდავს ინფორმაციას შემდეგი სახით:
# Name: Lia
# Surname: Kebadze
# Age: 20
# City: Tbilisi
print("3rd task")
name = input("Enter your name:")
surname= input("Enter your surname:")
age = input("Enter your age:")
city = input("Enter your city:")
print("Name: "+name)
print("Surname: "+surname)
print("Age: "+age)
print("City: "+name)
 
#4 დაწერე პროგრამა, რომელიც გთხოვს შეიყვანო ნებისმიერი სამი სხვადასხვა ხილის დასახელება ცალცალკე. რეზულტატი კი იბეჭდება შემდეგი სახით:
#  Apple//Peach%%Orange
print("4th task")
fruit1 = input("Enter fruit 1:")
fruit2 = input("Enter fruit 2:")
fruit3 = input("Enter fruit 3:")
print(fruit1+"//"+fruit2+"%"+"%"+fruit3)

#5 დაწერე პროგრამა, რომელიც გთხოვს შეიყვანო ტექსტი, დათვლის მასში არსებული სიმბოლოების რაოდენობას და გამოიტანს შედეგს შემდეგნაირად:
print("5th task")
txt = input("Enter text:")
print(len(txt))