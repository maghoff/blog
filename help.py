#!/usr/bin/env python
# -*- coding: utf-8 -*-

import optparse, textwrap

usage = "help [command]"
desc = "Display documentation about commands"

longhelp = """
Run help with no arguments to display a list of all available commands.

If the name of a command is given as an argument, detailed help about
this command will be given.
"""

def run(argv):
	p = optparse.OptionParser()

	(options, args) = p.parse_args(argv)

	if len(args) >= 1:
		tw = textwrap.TextWrapper()
		tw.initial_indent = '    '
		tw.subsequent_indent = '    '
		c = args[0]

		cmd = __import__(c)
		print "%s\n\n%s\n" % (cmd.usage, cmd.desc)
		for p in cmd.longhelp.strip().split('\n\n'):
			p = p.strip()
			if len(p) == 0: continue
			print tw.fill(p)
			print
	else:
		# TODO: Find list of available commands
		cmds = [
			'help',
			'init',
			'publish',
		]

		print "Available commands:"
		for c in cmds:
			cmd = __import__(c)
			print "\t%s\t%s" % (c, cmd.desc)
		print

	return 0


if __name__ == '__main__':
	import sys
	sys.exit(run(sys.argv[1:]))
