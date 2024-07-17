def count_vowels(word):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

for word in words:
    vowel_count = count_vowels(word)
    print(f"{word}has {vowel_count} vowels")