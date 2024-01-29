#დაწერე კოდი რომელიც article.txt _დოკუმენტში იპოვის რიგით მეორე ყველაზე ხშირად განმეორებად სიტყვას.
def secondMostUsedWord(article):
    f = open(article, "r")
    content = f.read()
    words = content.lower().split()
    word_counts = {}
    for word in words:
        word = word.strip(".,!?;:'\"()[]{}")
        word_counts[word] = word_counts.get(word, 0) + 1
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    if len(sorted_word_counts) >= 2:
        second_most_common_word = sorted_word_counts[1][0]
        return second_most_common_word
    else:
        return None
#names.csv ფაილში არსებული ინფორმაცია გადმოაკოპირე names.txt ფაილში.
def copy_csv_to_text(csv_file, txt_file):
    with open(csv_file, 'r') as csv_file:
        with open(txt_file, 'a') as txt_file:
            for line in csv_file:
                txt_file.write(line)