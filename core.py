#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

CONFIG_FILE = u'.blog'

def walk_up(path):
	path = os.path.normpath(path)
	yield path
	while path != '/':
		path = os.path.split(path)[0]
		yield path

def find_config():
	for p in walk_up(os.getcwdu()):
		candidate = os.path.join(p, CONFIG_FILE)
		if os.path.isfile(candidate): return candidate
	return None

