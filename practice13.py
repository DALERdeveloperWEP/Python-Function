def is_palindrome(text: str):
    return text == text[::-1]

word = input("Text kiriting: ")

if is_palindrome(word):
    print("Palindrome")
else:
    print("Palindrome emas")
