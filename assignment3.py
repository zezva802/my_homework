from random import randint
#1. ჯეირანის პროგრამა
#  დაასრულე ჯეირანის თამაშის პროგრამა ციკლის გამოყენებით.
#  თამაშის დასასრულებლად რომელიმე მოთამაშემ უნდა დააგროვოს 3 ქულა.
print("-----------------task 1-----------------")
score1 = 0
score2 = 0 
p1name = input("sheiyvane saxeli: ")
p2name = input("sheiyvane mowinaagmdegis saxeli: ")
while score1 != 3 and score2 != 3:
    print(f"{p1name} {score1} - {score2} {p2name}")
    
    
    p1 = int(input("sheiyvane ras aketeb: 1 - cha, 2 - bade, 3 - makrateli"))
    p2 = randint(1,3)
    print(f"shen gaakete {'cha' if p1 == 1 else 'bade' if p1 == 2 else 'markateli'}")
    print(f"{p2name} gaaketa {'cha' if p2 == 1 else 'bade' if p2 == 2 else 'markateli'}")
    if p1 == p2:
        print("fre")
        continue
    elif p1 == 1:
        if p2 == 2:
            print(f"{p2name} +1 qula")
            score2 += 1
            continue
        if p2 == 3:
            print(f"{p1name} +1 qula")
            score1 += 1
            continue
    elif p1 == 2:
        if p2 == 3:
            print(f"{p2name} +1 qula")
            score2 += 1
            continue
        if p2 == 1:
            print(f"{p1name} +1 qula")
            score1 += 1
            continue
    elif p1 == 3:
        if p2 == 1:
            print(f"{p2name} +1 qula")
            score2 += 1
            continue
        if p2 == 2:
            print(f"{p1name} +1 qula")
            score1 += 1
            continue
print(f"{p1name} {score1} - {score2} {p2name}")
print(f"{p1name if score1>score2 else p2name} gaimarjva")

#2. გამრავლების ტაბულა
# ორმაგი for ციკლის დახმარებით დაბეჭდე გამრავლების ტაბულა
# 1_დან მომხმარებლის მიერ შეყვანილი მთელი რიცხვის ჩათვლით.

print("-----------------task 2-----------------")
table = int(input("sheiyvane sadamde gsurs gamravlebis tabulis tema"))
print("  ", end=" ")
for d in range(1,table + 1):
    if d == table:
        print(d)
    else:
        print(d, end=" ")
for i in range(1, table + 1):
    print(f"{i}|", end=" ")
    for j in range(1,table + 1):
        if j == table:
            print(i*j)
        else:
            print(i*j, end=" ")

#3. საბანკო ანგარიში 
#  შეადგინე პროგრამა რომელიც განასახიერებს საბანკო ანგარიშს.
#  მასზე განთავსებულია თანხა 3000 ლარის ოდენობით.
#  პროგრამა გეკითხება გაწეულ ხარჯს და აკლებს ანგარიშს მანამ, სანამ არ შეიყვან 0_ს.
#  შემდეგ გიბეჭდავს ანგარიშზე დარჩენილ თანხას და წყვეტს ფუნქციონირებას.
#  თუ ანგარიშზე არსებული თანხა ნაკლებია დანახარჯის თანხაზე, პროგრამამ უნდა დაბეჭდოს,
#  რომ ანგარიშზე არ არის საკმარისი თანხა და გააგრძელოს ფუნქციონირება.

print("-----------------task 3-----------------")
bal = 3000
while True:
    print(f"balansi: {bal}lari")
    cost = int(input("sheiyvane xarji: "))
    if cost==0:
        print(f"balansi: {bal}")
        break
    elif cost > bal:
        print("arasakmarisi tanxa angarishze!")
    else:
        bal -=cost

#4. თუთიყუშის პროგრამა 
# დაწერე პროგრამა თუთიყუში.
# პროგრამამ უნდა გაიმეოროს რასაც ეტყვი მანამ სანამ არ შეიყვან სიტყვას quit, 
# თუმცა წინ დაურთოს კითხვა „User Said Whaaat!?” თუ შევიყვანეთ სიტყვა Hello დაიბეჭდება 
# „User Said Whaaat!?”
# “User Said Hello”

print("-----------------task 4-----------------")
while True:
    phrase = input("i am listening... ")
    if phrase == "quit":
        print("OK, i am silent")
        break
    else:
        print("„User Said Whaaat!?”")
        print(f"„User Said {phrase}”")




        


        



