import re

text = input("Enter a string: ")
s = input("Enter a pattern to search: ")

match = re.search(s, text)

if match:
    print(f"Pattern '{s}' starts at {match.start()}")

else:
    print("Not found")

sp = re.split(r'\s+', text)
print("Split string:", sp)

replace = input("Enter a pattern to replace: ")
c = input("Enter new string: ")

new = re.sub(replace, c, text)

print("String after replacement:", new)