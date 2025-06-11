# Define vowel set
vowels = 'aeiouAEIOU'

# Initialize counters
vowel_count = 0
consonant_count = 0
uppercase_count = 0
lowercase_count = 0

# Open the file for reading
with open('data.txt', 'r') as file:
    for line in file:
        for char in line:
            if char.isalpha():  # Check if it's a letter
                if char in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1

                if char.isupper():
                    uppercase_count += 1
                elif char.islower():
                    lowercase_count += 1

# Display the results
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("Uppercase letters:", uppercase_count)
print("Lowercase letters:", lowercase_count)
