#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gdata, gdata.service, atom, util

def printit(blogger_service):
	query = gdata.service.Query()
	query.feed = '/feeds/default/blogs'
	feed = blogger_service.Get(query.ToUri())

	print feed.title.text
	for entry in feed.entry:
		print "\t" + entry.title.text, "blog_id:", entry.GetSelfLink().href.split("/")[-1]
