#!/usr/bin/env python3
import sys
import bs4
import requests

sys.stderr.write("Retrieving Synonyms...\n")

# check for correct arguments
if not len(sys.argv) > 1:
	print("Error, enter argument correctly.")
	exit()

res = requests.get('https://www.thesaurus.com/browse/' + sys.argv[1] +'?s=t')
lines_to_read = [7]

soup = bs4.BeautifulSoup(res.text, 'html.parser')

f = open("/home/red/wordscrape/" + "syn.txt", "w")
f.write(str(soup.textarea))
f.write(soup.prettify())
f.close()

rfile = open("/home/red/wordscrape/" + "syn.txt")

print("Thesaurus synonyms:")

for position, line in enumerate(rfile):
	if position > 900 and position < 1000:
		line = line.strip()
		if line[0] != "<":
			line = line.replace("\n", "")
			print(line, end =', ')
print('')
