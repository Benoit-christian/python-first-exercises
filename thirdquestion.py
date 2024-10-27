def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in text if char not in vowels)
user_input = input('Please enter a string of text')
user_output = remove_vowels(user_input)
print(user_output)