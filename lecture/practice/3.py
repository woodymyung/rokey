import re

text = "Call me at 010-1234-5678 or 010-987-6543."

pattern = r'010-\d{3,4}-\d{4}'
result = re.findall(pattern, text)
print(result)