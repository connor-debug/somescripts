#!/usr/bin/env python3
import sys
import bs4
import requests

# check for correct arguments
if not len(sys.argv) > 1:
	print("Error, enter argument correctly.")
	exit()

print("Attempting to retrieve definition...\n")

res = requests.get('https://dictionary.com/browse/' + sys.argv[1] + '?s=t')
line_to_read = [7] # dictionary.com web page

soup = bs4.BeautifulSoup(res.text, 'html.parser')

f = open("/home/red/wordscrape/" + "dict.txt", "w")
f.write(str(soup.textarea))
f.write(soup.prettify())
f.close()

rfile = open("/home/red/wordscrape/" + "dict.txt")

for position, line in enumerate(rfile):
	if position in line_to_read:
		line = line[17:]
		line = line[:len(line) - 32]
		print(line)
print('')
