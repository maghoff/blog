#!/usr/bin/env python
# -*- coding: utf-8 -*-

import optparse
import core, blogger, blogger.update

usage = "publish [--write]"
desc = "Publish to your blogger.com-blog"

longhelp = """
This command will look at the entries in your local blog and compare them
to the entries in your blogger.com-blog. Changed entries will be updated
and new entries will be added.

Nothing will be sent to blogger.com unless the --write-parameter is
supplied.
"""

def run(argv):
	p = optparse.OptionParser()

	p.add_option(
		"-w", "--write", dest="write", default=False, action='store_true',
		help = "Actually write data to blogger.com"
	)

	(options, args) = p.parse_args(argv)

	bs = blogger.get_blogger_service()
	blog_id = blogger.get_blog_id(bs)

	blogger.update.update(
		dry_run = not options.write,
		bs = bs,
		blog_id = blog_id,
		
	)

	return 0

if __name__ == '__main__':
	import sys
	sys.exit(run(sys.argv[1:]))
