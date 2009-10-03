#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, ConfigParser

PROJECT_CONFIG_FILE = u'.blog'
USER_CONFIG_FILE = u'~/.blog.user'

project_config_parser = None
user_config_parser = None

def walk_up(path):
	path = os.path.normpath(path)
	yield path
	while path != '/':
		path = os.path.split(path)[0]
		yield path

def find_config():
	for p in walk_up(os.getcwdu()):
		candidate = os.path.join(p, PROJECT_CONFIG_FILE)
		if os.path.isfile(candidate): return candidate
	return None

project_config_file = find_config

def user_config_file():
	return os.path.expanduser(USER_CONFIG_FILE)

def user_config():
	global user_config_parser
	if user_config_parser == None:
		user_config_parser = ConfigParser.RawConfigParser()
		user_config_parser.read(user_config_file())
	return user_config_parser

def acquire_user_setting(section, field, desc):
	cfg = user_config()

	if not cfg.has_section(section):
		cfg.add_section(section)

	if not cfg.has_option(section, field):
		cfg.set(section, field, ask(desc))

	return cfg.get(section, field)

def write_configs():
	global project_config_parser, user_config_parser

	if project_config_parser != None:
		fn = project_config_file()
		project_config_parser.write(open(fn, 'wb'))
		print "Wrote config to %s" % fn

	if user_config_parser != None:
		fn = user_config_file()
		user_config_parser.write(open(fn, 'wb'))
		print "Wrote config to %s" % fn



def ask(query):
	# Pluggable UI would be neat
	return raw_input(query + ': ')
