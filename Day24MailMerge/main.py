print('--------------------------------------------')
print("\nWelcome to Mail Merge\n")
print('--------------------------------------------')
print("This program will help you generate personalized letters for a list of recipients.\n")
print("Please ensure you have a 'letter.txt' file with a placeholder [name] for the recipient's name.")
print('add the names of the recipients in a file called "names.txt", with one name per line.\n')

while input('Do you wish to continue? [y/n] ').lower() == 'y':
    # Read the letter template
    with open('letter.txt', 'r') as f:
        letter_template = f.read()
    # Read the names from the names file
    with open('names.txt', 'r') as f:
        names = f.readlines()
    # Generate personalized letters
    for name in names:
        name = name.strip()  # Remove any leading/trailing whitespace
        personalized_letter = letter_template.replace('[name]', name)
        # Save the personalized letter to a new file
        with open(f'ReadyToSend/letter_for_{name}.txt', 'w') as letter_file:
            letter_file.write(personalized_letter)
    print("Personalized letters have been generated and saved as 'letter_for_<name>.txt' in the 'ReadyToSend' folder.")
    print('--------------------------------------------')
