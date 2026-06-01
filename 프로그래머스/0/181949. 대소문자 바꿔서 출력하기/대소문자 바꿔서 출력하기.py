str=input()
new_str = ""
for i in range(len(str)):
    if ord(str[i]) < 97 :
        new_str += str[i].lower()
    else:
        new_str += str[i].upper()
print(new_str)