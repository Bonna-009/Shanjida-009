def check_character():
    char = input("Enter a single character: ").lower()

    if len(char) != 1 or not char.isalpha():
        print("Please enter a single alphabetic character.")
        return

    vowels = 'aeiou'

    if char in vowels:
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is a consonant.")
