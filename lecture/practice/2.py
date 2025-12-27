import re

text = """
Info: Operation success
Error: File not found
Warning: Disk full
Error: Network timeout
"""

pattern = re.compile('^Error.*', re.MULTILINE)
result = pattern.findall(text)

print(result)