import re
from base64 import b64decode
def find_and_print_alphanumeric(input_text):
    pattern = r'([a-zA-Z0-9]+[=]{1,2})'
    matches = re.findall(pattern, input_text)
    for match in matches:
        print(b64decode(match).decode("ascii"))
input_text = open("records.txt").readline()
find_and_print_alphanumeric(input_text)