#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys
import yabormeparser.announcement.nombramientos as n


def is_unknown(position):
    for p in positions:
        if position.endswith(p):
            return False
    return True


def nombramientos(value):
    chunks = value.split(":")[0:-1]
    unknown = []
    for c in chunks:
        if is_unknown(c.upper()):
            unknown.append(c)
    return unknown

positions = n.position.keys()


def get_unknown_positions(file_):
    errors = json.load(open(file_))
    unknown = []
    for e in errors:
        if e['label'] == "Nombramientos" or e['label'] == "Ceses/Dimisiones":
            unknown += nombramientos(e['value'])
    return set(unknown)


if __name__ == "__main__":
    file_ = 'ERRORS.json'
    test = "Vcp.Cons.Rec: JULIAN LAGUNA GARCIA. Mie.Cons.Rec: JULIAN LAGUNA GARCIA. Sec.Cons.Rec: MIGUEL ANGEL PASCUAL SANCHO. Mie.Cons.Rec: MIGUEL ANGEL PASCUAL SANCHO. Pre.Cons.Rec: JUAN ANTONIO LOPEZ PASCUAL. Mie.Cons.Rec: JUAN ANTONIO LOPEZ PASCUAL."
    # print nombramientos(test)
    if sys.argv:
        file_ = sys.argv[1]
    print "\n".join(get_unknown_positions(file_))
