import re

text = "Price: $12, Quantity: 3, Code: A82"

result = re.findall(r'\d+', text)

print(result)