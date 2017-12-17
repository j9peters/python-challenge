# Riddle 4
# URL:  http://www.pythonchallenge.com/pc/def/linkedlist.php

# View page source, locate partial URL:  linkedlist.php?nothing=12345

# Navigate to http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345

# Current page's 'nothing' number -> found in current page's URL
# Next page's 'nothing' number -> found in current page's text

import urllib.request

def URL_build(startlink):
    """
    Navigate through web pages that are linked via 'nothing' numbers.

    Return tuple containing the 'nothing' value in current URL and text on current page.
    """
    for i in range(0,400):
        with urllib.request.urlopen(startlink) as link:
            text = link.read().decode('utf-8')
            if "the next nothing is " in text:
                nextnumber = text[text.index("the next nothing is ")+20:]
                startlink = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+nextnumber
            else:
                break
    return (nextnumber, text)

print(URL_build("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"))

# Output:  ('16044', 'Yes. Divide by two and keep going.')

# The next page's 'nothing' = 16044/2 = 8022

print(URL_build("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022"))

# Output:  ('66831', 'peak.html')

# URL to Riddle 5:  http://www.pythonchallenge.com/pc/def/peak.html
