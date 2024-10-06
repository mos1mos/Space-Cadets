import sys
import re
import urllib.request

if len(sys.argv) != 2: # Making sure user used correct format
    print("Usage: p1.py [user_id]")
    sys.exit()
user_id = sys.argv[1] # Getting user_id from command line
try: # typing url into web and getting url back with persons name if it is a real web page
    url = "https://www.southampton.ac.uk/people/" + user_id
    newurl = urllib.request.urlopen(url).geturl()
except urllib.error.URLError: # catching error of couldnt open web page
    print("URLError, potentially your internet connection?")
    sys.exit()
pos = re.search(user_id, newurl) # Using regular expressions to search for user_id in url, text after that is user name
if pos is None: # If pos is none then the name doesnt exist so system exits
    print("Name not found")
    sys.exit()
name = (newurl[pos.span()[1] + 1::]) # Getting name from url
print(name.replace("-"," ")) 

