import pyperclip
import os
# We define the Texts variable as an empty list.
texts = {}
file_name = "database.txt"

def update_texts():
    """
    This function is executed the first time the program is run
    and pulls the data in the database.txt file into the texts list.
    Args:
        None
    Returns:
    -------
    None.

    """
    # We check whether there is database.txt in the folder
    # where our Python script file is located.
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            # The reason we write global texts here is so that the changes 
            # we make in the function are valid everywhere.
            global texts
            # We assign all lines in database.txt to the lines variable.
            lines = file.readlines()
            
            for line in lines:
                # Here we throw all the data in database.txt into the texts list.
                key, value = line.strip().split(": ")
                texts[key] = value
    # Since the database.txt file is not on the computer, we create it.
    else:
        with open(file_name, "w") as file:
            # If there is data in the Texts list, we save it in database.txt.
            for key, value in texts.items():
                file.write(f"{key}: {value}\n")
    
def write(firstString, secondString):
    """
     This write function allows the new word pair to be registered in the database.txt 
     file and added to the texts list.

    Parameters
    ----------
    firstString : This firstString variable is the first word we receive from the user. 
    secondString : This secondString variable is the sentence to be copied to the clipboard.

    Returns
    -------
    None.

    """
    with open(file_name, "a") as file:
        texts[firstString] = secondString
        file.write("{}: {}\n".format(firstString,secondString))

update_texts()
# For the convenience of the user, I looped the program so that it runs 
# without the need to reopen the program.
while True:
    # We take input from the user and ask them what to copy to the clipboard.
    answer = input("What do you want to copy? (For quit the program enter 0)\n")
    # If the answer variable is in the texts list, we enter the if command.
    if answer in texts:
        # With the Pyperclip library, we copy the answer variable in our database to the clipboard.
        pyperclip.copy(texts[answer])
        print("Text " + pyperclip.paste() + " copied to clipboard.")
    # If input is 0, we end the program.
    elif answer == '0':
        # The break command causes the while loop to end and the program terminates
        # because there is no more code to execute.
        break
    # If the input value is not in the database, we enter this if command.
    else:
        print("There is no text for " + answer)
        # We ask the user if they want to save it.
        answer2 = input("Do you want to add to the database:")
        # If the lower case of the answer is yes, we take the string it wants to save 
        # and redirect it to the write function.
        # We could also write the following in the If command: 
        # if answer2.upper() == "YES":
        if answer2.lower() == "yes":
            addtext = input("Please write it: ")
            write(answer, addtext)