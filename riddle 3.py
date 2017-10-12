# Riddle 3
# URL:  http://www.pythonchallenge.com/pc/def/equality.html

import requests
import re

# View page source, parse through wall of text

# Get web page data
webpage = requests.get("http://www.pythonchallenge.com/pc/def/equality.html")

# Extract the relevant lines of text
webpage_text = webpage.text[21:]

# Riddle text:  "One small letter, surrounded by EXACTLY three big bodyguards on each of its sides."
# "small letter" = lowercase letter
# "big bodyguard" = uppercase letter

pattern = re.compile('[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]')

# Matching 9-character sequences
charsequences = re.findall(pattern, webpage_text)

middlecharacters = ""

# Extract middle characters from 9-character sequences
for sequence in charsequences:
    middlecharacters += sequence[4]

print(middlecharacters)

# Output:  linkedlist

# Navigate to http://www.pythonchallenge.com/pc/def/linkedlist.html.  The text "linkedlist.php" is shown on the
# corresponding web page.

# URL to Riddle 4:  http://www.pythonchallenge.com/pc/def/linkedlist.php