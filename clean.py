import string 
import re 
text = str(input("Enter the text :-"))

text_lower = text.lower()
print(text_lower)

text_punch = re.sub(^[\w\s]','  ',text_lower)
print(text_punch)

text_clean =re.sub(r'\s+','  ',text_punch).strip()
print(text_clean)