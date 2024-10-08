# -*- coding:utf-8 -*-
#
# This work may be distributed and/or modified under the conditions of the LaTeX
# Project Public License, either version 1.3 of this license or (at your option)
# any later version.  The latest version of this license is in
#   http://www.latex-project.org/lppl.txt
# and version 1.3 or later is part of all distributions of LaTeX
# version 2005/12/01 or later.
#
# This work has the LPPL maintenance status `maintained'.
#
# The Current Maintainer of this work is Carlos Barth, carlos@cbarth.me
#
# This work consists of all files listed in manifest.txt.

from pandocfilters import toJSONFilter, RawBlock


def citacao(k, v, f, meta):
    if k == 'BlockQuote' and f == 'latex':
        begin = RawBlock('latex', u"\\begin{citacao}")
        end = RawBlock('latex', u"\\end{citacao}")
        return [begin] + v + [end]

if __name__ == "__main__":
    toJSONFilter(citacao)
