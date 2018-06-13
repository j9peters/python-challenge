# Riddle 6
# URL:  http://www.pythonchallenge.com/pc/def/channel.html

import zipfile
import os

# View page source, note the comment which reads
# "<!-- <-- zip -->".

# Navigate to http://www.pythonchallenge.com/pc/def/zip.html.  Note
# the text which reads, "yes. find the zip."  The text suggests that
# there is a zip file to discover.

# Navigate to "http://www.pythonchallenge.com/pc/def/channel.zip".
# A zip file named "channel.zip" will be downloaded to your computer.

# Save file to desired location and unzip.  A folder named "channel"
# will now be accessible.  Inside the folder, open the .txt file named
# "readme.txt".  Its contents read:
#
# "welcome to my zipped list.
#
# hint1: start from 90052
# hint2: answer is inside the zip"

# In the "channel" folder, there is a file named "90052.txt."  Open this
# file and note its contents, which read, "Next nothing is 94191."  The
# phrase "next nothing" was also used in Riddle 4.  This suggests that the
# solution to Riddle 6 may involve a methodology that is similar to that
# which was used in Riddle 4.  Web pages were linked together in Riddle 4
# via numbers.  Text files are linked together in this riddle via numbers
# as well.

# Iterate through the .txt files in the "channel" folder, beginning
# at the file named "90052.txt".  Each text file contains
# the phrase "Next nothing is " followed by a number.  The number
# indicates which text file to read next, since each text file's
# name is simply a number.
#
# Travel through the files until the pattern is broken, i.e. until
# a text file does NOT contain the phrase "Next nothing is ".
# Print the unique file's contents.

# Count the number of files in the "channel" folder
folder = os.listdir("/Users/Name/Downloads/channel")
numfiles = len(folder)

filename = "/Users/Name/Downloads/channel/90052.txt"

for i in range(0, numfiles):
    filehandler = open(filename, "r")
    filecontents = filehandler.read()
    filehandler.close()
    if "Next nothing is " in filecontents:
        nextfilenumber = filecontents.split()[-1]
        filename = "/Users/Name/Downloads/channel/" + nextfilenumber + ".txt"
    else:
        print(filecontents)
        break

# Output:
#
# Collect the comments.

# Each file examined in the above for loop has a zip file comment
# associated with it.  These comments are those which should be
# "collected."

channel_zipfile = zipfile.ZipFile("/Users/Name/Downloads/channel.zip", "r")

# Iterate through .txt files in the "channel" folder, as before, but print
# out the zip comment for each .txt file this time around.

filename = "/Users/Name/Downloads/channel/90052.txt"

for i in range(0, numfiles):
    filehandler = open(filename, "r")
    filecontents = filehandler.read()
    filehandler.close()
    print(channel_zipfile.getinfo(filename.split("/")[-1]).comment.decode('ascii'), end="")
    if "Next nothing is " in filecontents:
        nextfilenumber = filecontents.split()[-1]
        filename = "/Users/Name/Downloads/channel/" + nextfilenumber + ".txt"
    else:
        break

channel_zipfile.close()

# Output:
#
# ****************************************************************
# ****************************************************************
# **                                                            **
# **   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
# **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
# **   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
# **   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
# **   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
# **   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
# **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
# **   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
# **                                                            **
# ****************************************************************
#  **************************************************************

# Navigate to http://www.pythonchallenge.com/pc/def/hockey.html.  The web
# page reads, "it's in the air. look at the letters."  In examining the
# output "HOCKEY", each letter is formed from an arrangement of smaller
# letters.
#
# "H" is formed from "O's"
# "O" is formed from "X's"
# "C" is formed from "Y's"
# "K" is formed from "G's"
# "E" is formed from "E's"
# "Y" is formed from "N's"
#
# The smaller letters spell "oxygen", which is "in the air."

# URL to Riddle 7:  http://www.pythonchallenge.com/pc/def/oxygen.html