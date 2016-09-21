#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ply.lex
import ampliacion_de_capital
import ceses_dimisiones
import constitucion
import nombramientos
import common

_announcements = {
    u"Ampliación de capital": ampliacion_de_capital,
    u"Ceses/Dimisiones": ceses_dimisiones,
    u"Constitución": constitucion,
    u"Nombramientos": nombramientos
}


def process(label, value):
    announcement = None
    try:
        if label in _announcements:
            module = _announcements[label]
            ann = module.Parser(value)
            announcement = ann.to_dict()
    except ply.lex.LexError as e:
        raise common.ParserException(e)
    return announcement
