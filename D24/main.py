#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("D24\Input\Letters\starting_letter.txt") as letters:
    starting_letter = letters.readlines()
    # print(starting_letter)

with open(r"D24\Input\Names\invited_names.txt") as invited:
    invited_names_raw = invited.read()
    invited_names_list = invited_names_raw.splitlines()
    # invited_names_raw.replace("/n", "")
    # print(invited_names_list)


# print(starting_letter[0])
for names in invited_names_list:
    new_letter = starting_letter[0].replace("[name]", names)
    
    
    # print(new_letter)
    # for invited_names in starting_letter[1:]:
        # print(n)
    with open(f"D24\Output\\ReadyToSend\letter_for_{names}.txt", mode = "w") as letter:
        letter.write(new_letter)
        for content in starting_letter[1:]:
            letter.write(content)