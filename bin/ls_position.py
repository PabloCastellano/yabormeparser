#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import yabormeparser.announcement.nombramientos as nomb
import yabormeparser.announcement.common as common

if len(sys.argv) == 2:
    file_ = sys.argv[1]

lines = open(file_).readlines()

for l in lines:
    m = nomb.Lexer()
    m.build()
    # m.test(l)
    try:
        m.find_new_positions(l)
    except common.ParserException as e:
        print "ERROR: " + e.message[-20:]
