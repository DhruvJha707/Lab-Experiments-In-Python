'''Add few names, one name in each row, in “name.txt file”. 
a. Count no of names 
b. Count all names starting with vowel 
c. Find longest name '''


# --- Creating the file and writing names ---
with open("name.txt", "w") as f:
    f.write("Alice\n")
    f.write("Oscar\n")
    f.write("Bob\n")
    f.write("Uma\n")
    f.write("Charlotte\n")
    f.write("Ian\n")

# --- Reading and processing the file ---
with open("name.txt", "r") as f:
    names = [name.strip() for name in f.readlines()]

# a. Count number of names
count_names = len(names)

# b. Count names starting with vowels
vowels = ('A', 'E', 'I', 'O', 'U')
count_vowel_names = sum(1 for name in names if name.upper().startswith(vowels))

# c. Find longest name
longest_name = max(names, key=len)

# --- Output ---
print("Total names:", count_names)
print("Names starting with vowels:", count_vowel_names)
print("Longest name:", longest_name)
