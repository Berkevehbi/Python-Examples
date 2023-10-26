import pyperclip
import os

texts = {}

file_name = "veritabani.txt"

def write(firstString, secondString):
    with open(file_name, "a") as file:
        texts[firstString] = secondString
        file.write(f"{firstString}: {secondString}\n")

def update_texts():
    if os.path.exists(file_name):
        with open("veritabani.txt", "r") as file:
            global texts
            
            lines = file.readlines()
            
            for line in lines:
                key, value = line.strip().split(": ")
                texts[key] = value
            print(texts)
    else:
        with open("veritabani.txt", "w") as file:
            for key, value in texts.items():
                file.write(f"{key}: {value}\n")
update_texts()
print(texts)
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
        if answer2.lower() == "yes":
            addtext = input("Please write it: ")
            write(answer, addtext)