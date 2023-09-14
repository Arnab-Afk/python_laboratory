#dictionary to store the frequencies of the letter 
letter_frequency={}

#input from the user 
input_string=input("Enter a string: ")

#convert all the alphabets of the string to lowercase
input_lower=input_string.lower()


for char in input_lower:
    if char in letter_frequency:
        letter_frequency[char]+=1
    else:
        letter_frequency[char]=1

#delete all the whitespaces in the string
if(“ “ in letter_frequency)
del letter_frequency[‘ ‘] 



#loop to print the dictionary
for letter , frequency in letter_frequency.items():
    print(f"'{letter}': '{frequency}'")
