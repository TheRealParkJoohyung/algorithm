str = input()
new_str = ""
for i in str:
    if i.islower():
        new_str += i.upper()
    else:
        new_str += i.lower()
print(new_str)