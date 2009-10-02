Mission statement
=================

I have come to realize that [in order to think properly, I need to write][essay]. I have started this project in order to help me, and possibly others, act on this realization.

[essay]: http://www.paulgraham.com/essay.html

<div style="
    border-style: solid;
    border-width: 1px;
    margin: 1ex;
">This project will provide a command line tool to aid in writing and publishing a blog as part of a programming project.</div>


The command line tool should fit my regular workflow when programming, so it should sport an interface similar to that of popular [source code management][SCM] tools such as [Mercurial][hg]. The interface should be suited to serve as a back-end for graphical user interfaces, but this project will not provide such an interface.

[SCM]: http://en.wikipedia.org/wiki/Revision_control
[hg]: http://mercurial.selenic.com/wiki/


The syntax of the blog is [Markdown][md]. The Markdown-module of this project should of course be isolated and possible to exchange with other engines, but it is not considered important to actually supply alternative engines.

[md]: http://daringfireball.net/projects/markdown/


I feel very strongly about owning your data. This blogging tool will facilitate that by:

 * Keeping the blog entries as files in your project directory. Manage them with your [SCM][SCM] and you own the blog just as much as you own the source.
 * Providing a very plain "as HTML" "publishing"-method, to make sure that you never need to depend on a third party to have a blog.

However, publishing to [Blogger](http://www.blogger.com) will be the central feature, and a good way to make sure you can handle all traffic in the world without actually paying a dime. Not that your, or indeed my, blog will ever get any traffic, but it is good to feel safe :)
