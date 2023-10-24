import pyperclip
import csv

texts = {'agree' : 'Yes, I can come with you!', 
        'busy': 'No, I can not come with you. May we do this another time?',
        'no': "No, I don't want do this"
        }

def writerr(firstString, secondString):
    with open("veritabani.csv", "w", newline="") as csv_file:
        texts[firstString] = secondString
        csv_writer = csv.DictWriter(csv_file, fieldnames=texts.keys()) 
        csv_writer.writeheader()
        csv_writer.writerow(texts)
        print(texts)
def readerr():
    with open("veritabani.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            print(line)
def update_texts():
    global texts
    texts = [*csv.DictReader(open('veritabani.csv'))] 
    print(texts)
update_texts()
while True:
    answer = input("What do you want to copy?\n")

    if answer in texts:
        pyperclip.copy(texts[answer])
        print("Text " + pyperclip.paste() + " copied to clipboard.")
    elif answer == '0':
        break
    else:
        print("There is no text for " + answer)
        answer2 = input("Do you want to add to the database:")
        if answer2 == "Yes" or answer2 == "yes":
            addtext = input("Please write it: ")
            writerr(answer, addtext)
            update_texts()