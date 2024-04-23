# write file
# name = input("What's your name? ")

# with open("names.txt" , "a") as file:
#     file.write(f"{name}\n")

#read file
# with open("names.txt", "r") as file:
#     for line in file:
#         print("Hello,", line.rstrip())

#read file in sorted way
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")

# read file in sorted way(compacted version)
# names = []

# with open("names.txt") as file:
#     for line in sorted(file, reverse= True):
#         print(f"hello, {line.rstrip()}")