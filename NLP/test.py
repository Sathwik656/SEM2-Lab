import re

#Date matching
text = ""

p = (r"\b(0[1-9]|[1-2][0-9]|3[0-1])/(0[1-9]|1[1-2])/\d{4}\b")
data = re.findall(p.replace('(','(?:'),text)
print("Dates found: ",data)

password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?#&])[a-zA-Z\d@$!%*?#&],{8,}$"
password = "Heightgummi#78"
if re.match(password_pattern,password):
    print("Password is valid")
else:
    print("Password id valid")

#Match hexadecimal color codes
text = "The color code is"
hexpat = r'#(?:[A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})\b'
print("Hexadecimal color codes fond: ",re.findall(hexpat,text))
