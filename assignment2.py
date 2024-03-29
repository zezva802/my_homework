#1. ვიქტორინა
#შეადგინე ვიქტორინის პროგრამა. 
#მომხმარებელს უნდა დავუსვათ კითხვა: 
#“რომელი იმპერიის მიერ აგებული წყალ-მომარაგების სისტემა(აკვედუკი) ფუნქციონირებს დღესაც?”
#სავარაუდო პასუხები: 
#1.შუმერთა 
#2.სელჩუკთა
#3.რომის
#4.მონღოლთა 
#მომხმარებელმა უნდა შეიყვანოს სწორი პასუხის ნომერი ან თავად სწორი პასუხი. 
#შეცდომის შემთხვევაში იბეჭდება: „არა! სწორი პასუხია რომის!“ 
#სწორი პასუხის შემთხვევაში იბეჭდება: „სწორია!“
print("task 1:")
answer = input("რომელი იმპერიის მიერ აგებული წყალ-მომარაგების სისტემა(აკვედუკი) ფუნქციონირებს დღესაც?")
if answer == "3" or answer == "რომის":
    print("სწორია!")
else:
    print("არა! სწორი პასუხია რომის!")

#2. ონლაინ მაღაზია 
#პროგრამა გთავაზობს პროდუქტის სამ კატეგორიას.
#მაგ.
#1.ლეპტოპები
#2.პერსონალური კომპიუტერები
#3.მობილურები
#მომხმარებელი ირჩევს ერთ-ერთს.
#პროგრამა ითხოვს მაქსიმალურ ბიუჯეტს და ბიუჯეტის მიხედვით სთავაზობს მომხმარებელს კონკრეტულ მოდელს არჩეულ კატეგორიაში.
#(თითო კატეგორიაში მინიმუმ 3 პროდუქტი მაინც უნდა იყოს) 
#თუ ბიუჯეტი ძალიან მცირეა, პროგრამა ბეჭდავს, რომ ამ თანხაში არ გააჩნია შემოთავაზება.
print("task 2:")
print("კატეგორიები:")
print("1. ლეპტოპები")
print("2. პერსონალური კომპიუტერები")
print("3. მობილურები")
category = input("შეიყვანე კატეგორიის ნომერი:")
budget = input("შეიყვანე ბიუჯეტი:")
if category == "1":
    if budget >= "3000":
        print("ლენოვო, 3000 ლარად")
    elif budget >= "2000":
        print("სამსუნგი, 2000 ლარად")
    elif budget >= "1000":
        print("მაკბუკი, 1000 ლარად")
    else:
        print("ამ თანხაში შემოთავაზება არ გამაჩნია")
elif category == "2":
    if budget >= "3000":
        print("ელჯი, 3000 ლარად")
    elif budget >= "2000":
        print("სამსუნგი, 2000 ლარად")
    elif budget >= "1000":
        print("სონი, 1000 ლარად")
    else:
        print("ამ თანხაში შემოთავაზება არ გამაჩნია")

elif category == "3":
    if budget >= "3000":
        print("შაომი, 3000 ლარად")
    elif budget >= "2000":
        print("სამსუნგი, 2000 ლარად")
    elif budget >= "1000":
        print("აიფონი, 1000 ლარად")
    else:
        print("ამ თანხაში შემოთავაზება არ გამაჩნია")

#ქუესთის შედგენა (Text Based Adventure Game) 
#დაწერე ერთმანეთში ჩასმული if-else კონსტრუქციების გამოყენებით
#მარტივი ტექსტზე დაფუძნებული სათავგადასავლო თამაში.
#მაგ. თავიდან პროგრამა ბეჭდავს მომხმარებლის ადგილსამყოფელს და სთავაზობს მოქმედების რამდენიმე ვარიანტს. 
#სხვადასხვა არჩევანის შემთხვევაში თამაში სხვადასხვანაირად ვითარდება. 

startingPlace = "რუსთავი"

print("შენ ახლა იმყოფები " + startingPlace +"ში")

country = input("აირჩიე სად გსურს იმოგზაურო: \n" + "ეგვიპტე" + "," + "ჩინეთი" + "," + "იტალია" + "," + "ინგლისი")

if (country != "ეგვიპტე" and country != "ჩინეთი" and country != "იტალია" and country != "ინგლისი"):
    country = input("აირჩიე ჩამოთვლილთაგან ერთ-ერთი!")

if (country == "ეგვიპტე"):
    print("კარგი არჩევანია, ხეოფსის პირამიდები გელოდება")
    death = input("ცდი შეიპარო პირამიდაში? 0 = არა, 1 = კი")
    if(death == "0"):
        print("არ ღირს, გარედანაც მშვენიერი სანახაობაა")
    else: 
        print("შენ მოგკლა შხამიანმა ისრებმა")

if (country == "ჩინეთი"):
    print("კარგი არჩევანია, ჩინეთის კედელი ნამდვილად კარგი სანახაობაა")
    death = input("არც ისე მაღალია, ჩახტები? 0 = არა, 1 = კი")
    if(death == "0"):
        print("წკიპზე ხარ გადარჩენილი")
    else: 
        print("არ უნდა გექნა, იმედია ფეხებს შეინარჩუნებ")

if (country == "იტალია"):
    print("კარგი არჩევანია, გლადიატორები არა, მაგრამ კოლიზეუმი ნამდვილად ადგილზეა")
    death = input("ამოტვიფრავ შენ სახელს? სამუდამოდ დარჩები ისტორიას 0 = არა, 1 = კი")
    if(death == "0"):
        print("კარგია, ვანდალიზმი დასჯადია")
    else:
        print("პოლიციამ დაგინახა. ისე კაი ადვოკატი ვიცი, ლაშა ჯანიბეგაშვილი ;)")

if (country == "ინგლისი"):
    print("კარგი არჩევანია, იქნებ შენ მაინც მიხვდე სტოუნჰენჯის საიდუმლოს")
    death = int(input("ვა რამხელა ქვებია, მიკარი ფეხი. 0 = არა, 1 = კი"))
    if(death == 0):
        print("კარგია")
    else:
        print("ვერ წააქციე")