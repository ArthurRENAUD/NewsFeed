#!/usr/bin/env python

# 2005-06-05

# Dump the contents of the feed with the name
#   given on the command line -- match is not case-sensitive.
#
#   Format is
#              TITLE :: DESCRIPTION

from newsfeed import ContentItem, NewsWire, SearchWire, config_file, console_encoding

import os, sys, string, cPickle

newfeeds = []
config   = {}

enc = console_encoding

newsfeeds, config = cPickle.load(open(config_file, 'rb'))

try: name = sys.argv[1]
except:
	print "Please supply a feed name."
	sys.exit(1)

for f in newsfeeds:
	if f.name.lower() == name.lower():
		for x in f.content:
			print x.title.encode(enc, 'replace'), "::", x.descr.encode(enc, 'replace')
