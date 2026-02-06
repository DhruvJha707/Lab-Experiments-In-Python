''' Program to count number of unique words in a given sentence using sets.'''


sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()

# Use a set to store unique words
unique_words = set(words)

# Count unique words
print("Number of unique words:", len(unique_words))
