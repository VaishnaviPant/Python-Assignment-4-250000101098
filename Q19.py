def palindrome(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")

palindrome("madam")