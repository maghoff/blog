#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gdata, gdata.service, atom, getpass
import core


def auth():
	SEC = 'blogger'

	user = core.acquire_user_setting(
		SEC, 'user',
		'Google ID'
	)

	passwd = getpass.getpass("Password for Google ID \"%s\": " % user)

	bs = gdata.service.GDataService(user, passwd)
	bs.source = 'duck-bloggerintegration-1.0'
	bs.service = 'blogger'
	bs.account_type = 'GOOGLE'
	bs.server = 'www.blogger.com'
	bs.ProgrammaticLogin()

	cfg = core.user_config()
	cfg.set(SEC, 'token', bs.GetClientLoginToken())

	return bs
