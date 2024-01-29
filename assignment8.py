# 1.დაწერე პროგრამა რომელიც გადაამრავლებს სიის ყველა წევრს კონკრეტულ რიცხვზე ლამბდას გამოყენებით.
lst = [1,2,3,4,5,6,7,8,9]
n = 2 #ricxvi razec gvinda gadavamravlot
newlst = list(map(lambda x: x*n,lst))
print(newlst)



# 2.დაწერე პროგრამა ლამბდას გამოყენებით, რომელიც გადაცემული სიის სიგრძეს დააბრუნებს, მას შემდეგ რაც წაშლის სიიდან ყველა სახელს რომელიც პატარა სიმბოლოთი იწყება. (გამოიყენე .isupper() მეთოდი)
def deletelowerlength(lst):
    return len(list(filter(lambda x: x[0].isupper(),lst)))

# 3.დაწერე პროგრამა რომელიც დააჯამებს სიაში არსებულ დადებით და უარყოფით რიცხვებს ცალცალკე. გამოიყენე ლამბდა ფუნქცია და filter.
lst = [1,2,-2,-2,3,-6]
positives = list(filter(lambda x:x>=0,lst))
negatives = list(filter(lambda x:x<0,lst))
def sumPosandNeg(accPos = 0,accNeg = 0,positives=[], negatives=[]):
    if len(positives) == 0 and len(negatives)==0:
        return [accPos,accNeg]
    hPos, *tPos = positives
    hNeg, *tNeg = negatives

    return sumPosandNeg(accPos + hPos, accNeg + hNeg,tPos,tNeg)
sumpos, sumneg = sumPosandNeg(positives=positives,negatives=negatives)
print(f"""dadebitebis jami: {sumpos}
        uaryofitebis jami: {sumneg}""")

# 4.დაწერე ბანკის ექაუნთის შექმნის, ანგარიშზე თანხის განთავსების და შემდგომ ექაუნთში შესვლის პროგრამა,
# არასწორი ინფორმაციის შეყვანა მომხმარებლისგან დააზღვიე try და except ბლოკის მეშვეობით.
def login(bal):
    print("warmatebit shexvedi accountze")

    while True:
        print(f"""balansi: {bal}, airchie moqmedeba: 
          tanxis shetana(0)
          tanxis gamotana(1)
          gamosvla(2)""")
        sel = input("")
        try:
            if sel == "0":
                amount = int(input("sheiyvane shesatani tanxa: "))
                bal += amount
                
            elif sel=="1":
                amount = int(input("sheiyvane gamosatani tanxa: "))
                if amount > bal:
                    print("arasakmarisi tanxa balansze")        
                else:
                    bal =- amount
            elif sel =="2":
                return bal
            else:
                print("ucnobi operacia!")
        except:
            print("xarvezi")
        

username = ""
password = ""
bal = 0
while True:
    print("""airchie operacia:
        registracia(0)
        accountze shesvla(1)
        programis gatishva(2)""")
    sel = input("")
    if sel =="0":
        username = input("sheiyvane axali saxeli: ")
        password = input("sheiyvane axali paroli: ")
        print("warmatebit daregistrirdi")
    elif sel =="1":
        putusername = input("sheiyvane saxeli: ")
        putpassword = input("sheiyvane paroli: ")
        if putusername == username and putpassword == password:
            bal = login(bal)
        else: print("araswori informacia")
    elif sel =="2":
        print("program closed!")
        break
    else:
        print("ucnobi operacia")









