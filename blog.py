#!/usr/bin/env python
# -*- coding: utf-8 -*-

import core

def main(argv):
	script = argv[0]
	argv = argv[1:]
	cmd_name = "help"
	if len(argv) > 0:
		cmd_name = argv[0]
		argv = argv[1:]

	try:
		cmd = __import__(cmd_name, globals(), locals(), [], 0)
	except ImportError:
		print "Command \"%s\" not found. Try:\n\t%s help\n" % (cmd_name, script)
		return -1

	retval = cmd.run(argv)

	core.write_configs()

	return retval

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
