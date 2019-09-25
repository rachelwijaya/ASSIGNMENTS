import string
def ignore_punctuation(words):
    return "".join(letter.lower() for letter in words if letter in string.ascii_letters)

def reversePal(words):
    return words[::1]

def palindrome(words):
    words = ignore_punctuation(words)
    reverse = reversePal(reverse)
    if (words == reverse):
        print("Yes it is a palindrome.")
    else:
        print("It is not a palindrome.")
        
words = input("Enter a phrase/word: ")
words = palindrome(words)