#!/usr/bin/bash

echo "Attempting to scrape for the word: $1..." 

defscrape.py "$1"
synscrape.py "$1"

echo " Web scrape complete."

