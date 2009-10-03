#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gdata, gdata.service, atom
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
