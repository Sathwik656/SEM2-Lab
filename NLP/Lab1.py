import re

#Date matching
text = "Hello my date of birth is 11/01/2004 and my friends birthday is 08/04/2004"
p = (r"\b(0[1-9]|[1-2][0-9]|3[0-1])/(0[0-9]|1[1-2])/\d{4}\b")
data = re.findall(p.replace('(','(?:'),text)
print("Dates found: ",data)

#Password matching
password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?#&])[a-zA-Z\d@$!%*?#&]{8,}$"
password = "Heightgummi#78"
if re.match(password_pattern,password):
    print("Password is valid")
else:
    print("Password is invalid")

#Find sentence with ?
txt = """
What is your name?
How are you doing? 
This is a test sentence.
"""
question_pattern = r"[^?]*\?"
questions = [line for line in txt.splitlines()
             if re.fullmatch(question_pattern,line)]
print("Questions found: ",questions)

#Match Hexadecimal color codes
text = "The color code for red is #FF0000 and for green is #00FF00."
hexpat = r'#(?:[A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})\b'
print("Hexadecimal color codes found: ",re.findall(hexpat,text))
