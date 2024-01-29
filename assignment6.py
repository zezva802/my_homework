#1. შექმენი ფუნქცია, რომელიც მომხმარებლისგან მიღებულ ინფორმაციას გაასამმაგებს და დაბეჭდავს შემდეგნაირად:
# input: “ablabdabdab” 
# Output: „Tripled: ablabdabdabablabdabdabablabdabdab“
def triple(info):
    print(f"Tripled: {str(info)*3}")
triple("sdds")
#2. შექმენი ფუნქცია, რომელიც მიიღებს მომხმარებლის წონას და დააბრუნებს მის წონას მთვარეზე.
# (მთვარის გრავიტაცია 6_ჯერ ნაკლებია დედამიწისაზე)
def moonweight(weight):
    return int(weight)/6
print(moonweight(60))
#3. შექმენი კალკულატორის ფუნქცია, რომელიც მიიღებს გამოსახულებას მომხმარებლისგან input() ფუნქციის დახმარებით
# (სამ მონაცემს_ პირველ რიცხვს, მოქმედებას(+ -* / ^), მეორე რიცხვს) მაგ. „2 * 6“.
#  ფუნქცია დაშლის სტრიქონს split()ფუნქციის გამოყენებით.
# დათვლის და დააბრუნებს შედეგს.
# გაითვალისწინე რომ რიცხვის შეყვანის მაგიერ სიმბოლოების შეყვანის შემთხვევაში უნდა დააბრუნოს ფუნქციამ შესაბამისი მესიჯი.
# ასევე ნულზე გაყოფა არშეიძ₾ება, ამ შემთხვევაშიც უნდა დააბრუნოს შესაბამისი მესიჯი. (დააბრუნოს და არა დაპრინტოს)
# def calculate(operation):

#     num1, operator, num2 = operation.split()

#     if not (num1.isdigit() and num2.isdigit()):
#         return "Error: input valid numbers"
    
#     num1 = float(num1)
#     num2 = float(num2)
    
#     if operator == "+":
#         return num1 + num2
#     elif operator == "-":
#         return num1 - num2
#     elif operator == "*":
#         return num1 * num2
#     elif operator == "/":
#         if num2 == 0:
#             return "Error: Division by zero"
#     elif operator == "^":
#         return num1 ** num2
#     else: 
#         return "Error: Invalid operator"

def calculate():
    operation = input("input operation: ")

    num1, operator, num2 = operation.split()

    if not (num1.isdigit() and num2.isdigit()):
        return "Error: invalid numbers"
    
    num1 = float(num1)
    num2 = float(num2)
    
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Error: Division by zero"
    elif operator == "^":
        return num1 ** num2
    else: 
        return "Error: Invalid operator"
print(calculate())

# p.s პირობიდან ვერ გავიგე input() ფუნქციაშივე უნდა ყოფილიყო თუ გარეთ, ორივენაირი დავწერე.


#გავლილი მასალის გამოყენებით შექმენი ფუნქცია, რომელიც მიიღებს ლათინურის იმბოლოებით დაწერილ სიტყვას,
# დაშიფრავს მორზეს ანბანით და დააბრუნებს შედეგს. 

def morsecode(symbol):
    symbol = symbol.upper()
    if symbol=="A":
        return ".-"
    elif symbol == "B":
        return "-..."
    elif symbol == "C":
        return "-.-."
    elif symbol == "D":
        return "-.."
    elif symbol == "E":
        return "."
    elif symbol == "F":
        return "..-."
    elif symbol == "G":
        return "--."
    elif symbol == "H":
        return "...."
    elif symbol == "I":
        return ".."
    elif symbol == "J":
        return ".---"
    elif symbol == "K":
        return "-.-"
    elif symbol == "L":
        return ".-.."
    elif symbol == "M":
        return "--"
    elif symbol == "N":
        return "-."
    elif symbol == "O":
        return "---"
    elif symbol == "P":
        return ".--."
    elif symbol == "Q":
        return "--.-"
    elif symbol == "R":
        return ".-."
    elif symbol == "S":
        return "..."
    elif symbol == "T":
        return "-"
    elif symbol == "U":
        return "..-"
    elif symbol == "V":
        return "...-"
    elif symbol == "W":
        return ".--"
    elif symbol == "X":
        return "-..-"
    elif symbol == "Y":
        return "-.--"
    elif symbol == "Z":
        return "--.."
    elif symbol == "0":
        return "-----"
    elif symbol == "1":
        return ".----"
    elif symbol == "2":
        return "..---"
    elif symbol == "3":
        return "...--"
    elif symbol == "4":
        return "....-"
    elif symbol == "5":
        return "....."
    elif symbol == "6":
        return "-...."
    elif symbol == "7":
        return "--..."
    elif symbol == "8":
        return "---.."
    elif symbol == "9":
        return "----."
    elif symbol == ".":
        return ".-.-.-"
    elif symbol == ",":
        return "--..--"
    elif symbol == "?":
        return "..--.."
    elif symbol == "\\":
        return ".----."
    elif symbol == "!":
        return "-.-.--"
    elif symbol == "/":
        return "-..-."
    elif symbol == "(":
        return "-.--."
    elif symbol == ")":
        return "-.--.-"
    elif symbol == "&":
        return ".-..."
    elif symbol == ":":
        return "---..."
    elif symbol == ";":
        return "-.-.-."
    elif symbol == "=":
        return "-...-"
    elif symbol == "+":
        return ".-.-."
    elif symbol == "-":
        return "-....-"
    elif symbol == "_":
        return "..--.-"
    elif symbol == '"':
        return ".-..-."
    elif symbol == "$":
        return "...-..-"
    elif symbol == "@":
        return ".--.-."
    else:
        return f"Invalid character {symbol}"

def converttomorse(text):
    code = ""
    for i in text:
        if i == " ":
            code +="/ "
        else:
            code += morsecode(i) +" "
    return code
print(converttomorse("testi 1 2"))




