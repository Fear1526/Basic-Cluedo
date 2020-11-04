# List of all characters
chars = ["Miss Scarlett","Professor Plum", "Mrs Peacock", "Reverend Green", "Colonel Mustard", "Dr Orchid"]

# For loop to go through length of array
for counter in range(len(chars)):
    # Prints each character one at a time
    print(chars[counter])
    # Asks the user to input if the character is guilty or not guilty
    user_input =  str(input("Guilty or Not Guilty?"))