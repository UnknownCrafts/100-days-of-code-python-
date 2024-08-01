# Mail merging using python

def read_letter(file_name):
    with open(file_name, "r") as file:
        return file.readlines()
    
def read_names(name_file):
    with open(name_file, "r") as file:
        return file.readlines()


letter_content = read_letter("./Input/Letters/starting_letter.txt")
names = read_names("./Input/Names/Invited_names.txt")

for name in names:
    new_name = name.strip('\n')
    new_letter_content = letter_content[:]
    new_letter_content[0] = new_letter_content[0].replace("[name]", new_name)
    with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", "w") as file:
        file.writelines(new_letter_content)
            