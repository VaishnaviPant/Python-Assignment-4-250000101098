def count_vowels(s):
    count = 0

    for ch in s.lower():
        if ch in "aeiou":
            count += 1

    print("Number of vowels:", count)

count_vowels("Python Programming")