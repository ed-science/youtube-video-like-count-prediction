import re

def charCount(text):
    return len(text) - text.count(' ')

def wordCount(text):
	return len(text.split())

def containsWebsite(text):
    return 1 if re.search('http://', text, re.I) is not None else 0

def containsSocialMedia(text):
	# facebook.com
	# twitter.com
	# instagram.com
	# fb.me
	# t.co
	# instagr.am
	if re.search('facebook\.com|twitter\.com|instagram\.com|fb\.me|t\.co|instagr\.am', text, re.I) is not None:
		return 1
	return 0
