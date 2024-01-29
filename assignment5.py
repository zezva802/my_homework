#ციკლის მეშვეობით 3 მომხმარებელს შეაყვანინე ინფორმაცია საკუთარი სახელის, გვარის და ასაკის შესახებ.
# თითოეული მომხმარებლის ინფორმაცია შეინახე ინდივიდუალურ სიაში.
# შემდეგ კი სამივე სია დაამატე საერთო ცალრიელ სიას სახელად consumer_info.
# Input_ის მეშვეობით მომხმარებლის ინდექსის შეყვანის შემთხვევაში პროგრამამ უნდა დაბრუნოს არჩეულ მომხმარებელზე ინფორმაცია შემდეგნაირად:
# Name: Elene
# Lastname: Khardava
# Age: 21
print("---------------task 1---------------")
user1 = []
user2 = []
user3 = []
consumer_info = []

for i in range(3):
    if i == 0:
        user1 = input("sheiyvane user 0 is saxeli gvari asaki: ").split()
    elif i == 1:
        user2 = input("sheiyvane user 1 is saxeli gvari asaki: ").split()
    elif i == 2:
        user3 = input("sheiyvane user 2 is saxeli gvari asaki: ").split()

consumer_info.append(user1)
consumer_info.append(user2)
consumer_info.append(user3)

while True:
    i = input("sheiyvane momxmareblis indeqsi (0,1,2): ")

    if i == "quit":
        break
     
    print(f"Name: {consumer_info[int(i)][0]}\nLastname: {consumer_info[int(i)][1]}\nAge: {consumer_info[int(i)][2]}")
    print("dawere quit gamosasvlelad")

#მომხმარებელი დაარეგისტრირე ონლაინ პლატფორმაზე
# თუ სახელის ველი არ იქნება ცარიელი, ხოლო პაროლი 8 სიმბოლოზე მეტი ან ტოლია.
# მისი მონაცემები შეინახე ლისთში.
# შემდეგ მიეცი საშუალება სცადოს პლატფორმაზე შესვლა და შეადარე მის მიერ შემოყვანილი ინფორმაცია სიაში შენახულ ინფორმაციას.
# დაბეჭდე შესაბამისი მესიჯი.
print("---------------task 2---------------")
print("registracia")
info = []
#saxelis sheyvana da sisworis shemowmeba
while True:
    username = input("saxeli: ")
    if username == None:
        print("saxelis veli ar unda iyos carieli!")
    else:
        info.append(username)
        break

#parolis sheyvana da sisworis shemowmeba
while True:
    password = input("paroli: ")
    if len(password)<8:
        print("parolis veli unda iyos minimum 8 simbolo")
    else:
        info.append(password)
        break

print("accauntze shesvla")
while True:
    username_ = input("saxeli: ")
    if username_ == info[0]: #tu saxeli sworia mashin parolis sheyvana
        for i in range(3): #3 cda
            password_ = input("paroli: ")
            if password_ == info[1]:
                print("warmatebit shexvedit accountze")
                break
            else:
                print(f"paroli arasworia, {f'darchenilia {2-i} cda!' if 2-i > 0 else 'cdebi amoiwura, sheiyvanet saxeli axlidan!'}")
        else: #tu ar dabreakda eseigi 3jer arasworad sheiyvana amitom axlidan sheiyvanos saxeli (lupis axlidan dawyeba)
            continue
        break #tu for lupi dabreakda eseigi swori parolia sheyvanili da aq mtlian while lups vrtavt
    else:
        print("saxeli ar moidzebna! scadet axlidan.")

#შექმენი ჩაშენებული სია,
# რომელშიც იქნება შენახული ცნობილი მსახიობების შესახებ ინფორმაცია.
# მომხმარებელს შემოჰყავს მსახიობის სახელი ან გვარი.
# თუ სიაში მოიძებნა მსახიობი, 
# დაბეჭდე მის შესახებ არსებული ინფორმაცია რეზუმის სახით.
print("---------------task 3---------------")

actors = [['Robert', 'Deniro', 'Amerikeli', '"Goodfellas" "Taxi Driver" "Once Upon a Time in America" "The Godfather: Part II"', '2'], 
           ['Cristian', 'Bale', 'English', '"Ford v Ferrari" Batman trilogy "The Prestige" "The Pale Blue Eye"', '1'], 
           ['Daniel', 'Day-Lewis', 'English', '"There Will Be Blood" "In the Name of the Father" "Lincoln"', '3'], 
           ['Otar', 'Meghvinetukhutsesi', 'Qartveli', '"Data Tutashkhia" "Didostatis Marjvena" "Tetri Bairagebi"', '0'], 
           ['Emily', 'Blunt', 'British', '"Sicario" "Looper" "Edge of Tomorrow" "Oppenheimer"', '0'], 
           ['Anthony', 'Hopkins', 'Welsh', '"The Silence of the Lambs" "The Father" "The Elephant Man"', '2']]

while True:
    order = input("\nchawere msaxiobis saxeli an gvari, msaxiobebis siis sanaxavad chawere 'list', gamosasvlelad chawere 'quit'\n ")

    if order == "list":
        for actor in actors:
            print("\n"+actor[0]+" "+actor[1])
        continue

    elif order == "quit":
        break
    
    for actor in actors:
        if order in actor:
            print(f"\nsaxeli: {actor[0]}")
            print(f"\ngvari: {actor[1]}")
            print(f"\nerovneba: {actor[2]}")
            print(f"\ntop filmebi: {actor[3]}")
            print(f"\noskarebis raodenoba: {actor[4]}")
            break
    else:
        print("msaxiobi ar moidzebna, scade axlidan")
        
    
    


        
    


    