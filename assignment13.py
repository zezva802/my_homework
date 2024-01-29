import os

#დაწერე ფუნქცია რომელიც მომხმარებელს ჩააწერინებს ტექსტურ ფაილში ინფორმაციას Input ფუნქციის დახმარებით,
#მანამ სანამ მომხმარებელი არ შეიყვანს სიტყვას _ “enough”.
def write_to_file():
    with open("output.txt", "w") as file:
        while True:
            user_input = input("Enter text (type 'enough' to stop): ")
            if user_input == "enough":
                break
            file.write(user_input + "\n")

write_to_file()

#დაწერე ფუნქცია რომელიც input ფუნქციის დახმარებით მომხმარებლისგან მიიღებს საქაღალდის ლოკაციას და შესაქმნელი ფაილის სახელს,
#შემდეგ მიღებულ ლოკაციაზე შექმნის შესაბამის ფაილს და ამოპრინტავს საქაღალდეში არსებულ ყველა ფაილის სიას
def create_file_and_print_files():
    folder_location = input("Enter the folder location: ")
    file_name = input("Enter the file name: ")
    file_path = os.path.join(folder_location, file_name)

    with open(file_path, "w") as file:
        file.write("This is a new file.")

    file_list = os.listdir(folder_location)
    print("List of files in the folder:")
    for file in file_list:
        print(file)

create_file_and_print_files()
