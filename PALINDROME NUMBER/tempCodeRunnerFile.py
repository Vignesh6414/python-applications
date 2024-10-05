def palindrome(word):
    reverse = word[::-1]
    if word == reverse:
        print(f"This {word} is palindrome")
    else:
        print(f"This {word} is not palindrome")
palindrome(word=input("enter your choice"))