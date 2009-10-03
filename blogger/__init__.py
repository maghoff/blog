#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gdata, gdata.service, atom, itertools
import core

SECTION = 'blogger'

def get_blogger_service():
	cfg = core.user_config()
	
	if cfg.has_option(SECTION, 'token'):
		token = cfg.get(SECTION, 'token')
		bs = gdata.service.GDataService()
		bs.source = 'duck-bloggerintegration-1.0'
		bs.service = 'blogger'
		bs.account_type = 'GOOGLE'
		bs.server = 'www.blogger.com'
		bs.SetClientLoginToken(token)
		return bs
	else:
		import auth
		return auth.auth()

def get_blog_id(bs):
	cfg = core.project_config()

	if cfg.has_option(SECTION, 'blog_id'):
		return cfg.get(SECTION, 'blog_id')

	query = gdata.service.Query()
	query.feed = '/feeds/default/blogs'
	feed = bs.Get(query.ToUri())

	blog_id = None
	while blog_id == None:
		for entry, i in zip(feed.entry, itertools.count()):
			print " [%i] %s" % (i, entry.title.text)
		print " [n]: Create a new blog (not implemented)"

		c = None
		try:
			c = int(raw_input("Please choose which blog to publish to: "))
		except ValueError:
			c = None
		
		if c >= 0 and c < len(feed.entry):
			entry = feed.entry[c]
			blog_id = entry.GetSelfLink().href.split("/")[-1]

	cfg.add_section(SECTION)
	cfg.set(SECTION, 'blog_id', blog_id)
	
	return blog_id
