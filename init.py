#!/usr/bin/env python
# -*- coding: utf-8 -*-

import optparse, ConfigParser
import core

usage = "init"
desc = "Initialize blogging"

longhelp = """
In order for most blog commands to work, the working directory must
be at or below a directory previously initialized by this command.

This command will create a .blog-file in the current directory. When
other commands run they will look for this file upward in the
directory tree.

The .blog-file stores project wide configuration for blogging.
"""

def run(argv):
	p = optparse.OptionParser()

	(options, args) = p.parse_args(argv)

	config_file = core.find_config()

	if config_file != None:
		print "Existing config file found:", config_file
		print "Refusing to create a new config file"
		return -1

	cfg = ConfigParser.RawConfigParser()
	cfg.add_section('Filesystem')
	cfg.set('Filesystem', 'path', 'blog/')
	f = open('.blog', 'wb')
	cfg.write(f)
	f.close()

	print "Now use \"blog add\" to add a blog entry!"

	return 0

if __name__ == '__main__':
	import sys
	sys.exit(run(sys.argv[1:]))
