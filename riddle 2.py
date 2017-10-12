# Riddle 2
# URL:  http://www.pythonchallenge.com/pc/def/ocr.html

import requests

# View page source, parse wall of text

# Unique characters in wall of text
uniquechars = ""

# Get web page data
webpage = requests.get("http://www.pythonchallenge.com/pc/def/ocr.html")

# Extract the relevant lines of text, store each line as a list item
webpage_list = webpage.text.split("\n")[36:1258]

# Parse characters in each list item to identify unique characters
for item in webpage_list:
    for char in item:
        if char not in uniquechars:
            uniquechars += char

print(uniquechars)

# Output:  <!-%$@_^#)&+]*}[({equality>

# URL to Riddle 3:  http://www.pythonchallenge.com/pc/def/equality.html