# -*- coding:utf-8 -*-

from pandocfilters import toJSONFilter, RawBlock


def citacao(k, v, f, meta):
    if k == 'BlockQuote' and f == 'latex':
        begin = RawBlock('latex', u"\\begin{citacao}")
        end = RawBlock('latex', u"\\end{citacao}")
        return [begin] + v + [end]

if __name__ == "__main__":
    toJSONFilter(citacao)
