#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from yabormeparser.annoucement import ampliacion_de_capital


# BORME-A-2009-101-28

class TestAmpCap2009(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_2009_0(self):
        c = u"Capital: 72.144,00 Euros. Resultante Suscrito: 75.150,00 Euros."
        p = ampliacion_de_capital.Parser(c)
        self.assertEqual(p.capital, 72144.0)
        self.assertEqual(p.resultante_suscrito, 75150.0)
        self.assertEqual(p.suscrito, 0.0)
        self.assertEqual(p.desembolsado, 0.0)
        self.assertEqual(p.resultante_desembolsado, 0.0)

    def test_2009_1(self):
        c = u"Suscrito: 248.999,24 Euros. Desembolsado: 248.999,24 Euros. Resultante Suscrito: 4.760.122,36 Euros. Resultante Desembolsado: 4.760.122,36 Euros."
        p = ampliacion_de_capital.Parser(c)
        self.assertEqual(p.capital, 0.0)
        self.assertEqual(p.resultante_suscrito, 4760122.36)
        self.assertEqual(p.suscrito, 248999.24)
        self.assertEqual(p.desembolsado, 248999.24)
        self.assertEqual(p.resultante_desembolsado, 4760122.36)


# BORME-A-2014-...

class TestAmpCap2014(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # BORME-A-2014-199-17.RAW

    def test_2014_0(self):
        c = u"Capital: 5.000,00 Euros. Resultante Suscrito: 29.000,00 Euros."
        p = ampliacion_de_capital.Parser(c)
        self.assertEqual(p.capital, 5000.0)
        self.assertEqual(p.resultante_suscrito, 29000.0)
        self.assertEqual(p.suscrito, 0.0)
        self.assertEqual(p.desembolsado, 0.0)
        self.assertEqual(p.resultante_desembolsado, 0.0)


    def test_2014_1(self):
        c = u"Capital: 180.003,09 Euros. Resultante Suscrito: 189.018,27 Euros."
        p = ampliacion_de_capital.Parser(c)
        self.assertEqual(p.capital, 180003.09)
        self.assertEqual(p.resultante_suscrito, 189018.27)
        self.assertEqual(p.suscrito, 0.0)
        self.assertEqual(p.desembolsado, 0.0)
        self.assertEqual(p.resultante_desembolsado, 0.0)

    # BORME-A-2014-199-28

    def test_2014_2(self):
        c = u"Suscrito: 31.967,19 Euros. Desembolsado: 31.967,19 Euros. Resultante Suscrito: 673.247,11 Euros. Resultante Desembolsado: 673.247,11 Euros."
        p = ampliacion_de_capital.Parser(c)
        self.assertEqual(p.capital, 0.0)
        self.assertEqual(p.resultante_suscrito, 673247.11)
        self.assertEqual(p.suscrito, 31967.19)
        self.assertEqual(p.desembolsado, 31967.19)
        self.assertEqual(p.resultante_desembolsado, 673247.11)

    def test_2014_3(self):
        c = u"Capital: 2.813.428,00 Euros. Resultante Suscrito: 5.358.361,00 Euros."
        p = ampliacion_de_capital.Parser(c)
        self.assertEqual(p.capital, 2813428.0)
        self.assertEqual(p.resultante_suscrito, 5358361.0)
        self.assertEqual(p.suscrito, 0.0)
        self.assertEqual(p.desembolsado, 0.0)
        self.assertEqual(p.resultante_desembolsado, 0.0)

if __name__ == "__main__":
    unittest.main()
