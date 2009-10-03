#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gdata, gdata.service, atom
import core


def auth():
	SEC = 'blogger'

	user = core.acquire_user_setting(
		SEC, 'user',
		'Blogger.com (Google) ID, including @server'
	)

	passwd = core.ask("Password for %s (WARNING! Password will be echoed in plain text. Patches will be accepted.)" % user)

	bs = gdata.service.GDataService(user, passwd)
	bs.source = 'duck-bloggerintegration-1.0'
	bs.service = 'blogger'
	bs.account_type = 'GOOGLE'
	bs.server = 'www.blogger.com'
	bs.ProgrammaticLogin()

	cfg = core.user_config()
	cfg.set(SEC, 'token', bs.GetClientLoginToken())

	return bs
