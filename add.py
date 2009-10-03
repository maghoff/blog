#!/usr/bin/env python
# -*- coding: utf-8 -*-

import core, datetime, optparse, re, os, subprocess

usage = "add"
desc = "Add a blog entry"

longhelp = """
This command will create a new file in the blog-directory and
open it for editing.
"""

def get_latest_entry_no(root):
	latest = 0
	r = re.compile('^(\d\d)-\d\d\d\d-\d\d-\d\d-.*.md$')
	for f in os.listdir(root):
		m = r.match(f)
		if m: latest = max(latest, int(m.groups()[0]))
	return latest

def run(argv):
	p = optparse.OptionParser()

	(options, args) = p.parse_args(argv)

	root = core.get_blog_directory()
	
	latest = get_latest_entry_no(root)
	no = latest + 1

	d = datetime.date.today()

	title = "Temp"
	fn_pattern = "%02i-%04i-%02i-%02i-%s.md"
	o_fn = fn_pattern % (no, d.year, d.month, d.day, title)
	o_fn = os.path.join(root, o_fn)

	f = open(o_fn, 'wb')
	f.write("Title\n=====\n\n")
	f.close()

	subprocess.check_call([os.environ["EDITOR"], o_fn])

	f = open(o_fn, 'rb')
	title = f.readline().strip().replace(' ', '-')
	f.close()
	
	n_fn = fn_pattern % (no, d.year, d.month, d.day, title)
	n_fn = os.path.join(root, n_fn)

	os.rename(o_fn, n_fn)
	print "Wrote", n_fn

	return 0

if __name__ == '__main__':
	import sys
	sys.exit(run(sys.argv[1:]))
