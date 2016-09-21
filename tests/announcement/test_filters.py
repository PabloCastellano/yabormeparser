#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import yabormeparser.announcement.filters as filters


class TestPtasEuros(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ptas_to_euros_simple(self):
        # round(2000 / 166.39, 2) 12.02
        text = "2.000 Ptas."
        result = filters.ptas_to_euros(text)
        self.assertEqual("12,02 Euros.", result)

    def test_ptas_to_euros_simple2(self):
        # 3000 18.03
        text = u"3.000 Ptas."
        result = filters.ptas_to_euros(text)
        self.assertEqual(u"18,03 Euros.", result)

    def test_ptas_to_euros_nochange(self):
        # 3000 18.03
        text = u"Esto no se cambia 3.000 Patatas. 2.000 Euros."
        result = filters.ptas_to_euros(text)
        self.assertEqual(u"Esto no se cambia 3.000 Patatas. 2.000 Euros.",
                         result)

    def test_ptas_to_euros_context(self):
        # 3000 18.03
        text = u"Un puto royo 3.000 Ptas. Más mierda"
        result = filters.ptas_to_euros(text)
        self.assertEqual(u"Un puto royo 18,03 Euros. Más mierda", result)

    def test_ptas_to_euros_twice(self):
        # 3000 18.03
        text = u"Esto se cambia 3.000 Ptas. 2.000 Ptas."
        result = filters.ptas_to_euros(text)
        self.assertEqual(u"Esto se cambia 18,03 Euros. 12,02 Euros.",
                         result)


class DeleteDNI(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_dni_no_delete(self):
        text = u"NO DELETE NOTHING. : B123A."
        result = filters.delete_dni(text)
        expected = u"NO DELETE NOTHING. : B123A."
        self.assertEqual(expected, result)

    def test_dni_1(self):
        text = u"ADM.UNICO: RALUY AYATS JORGE. : 40875629Y."
        result = filters.delete_dni(text)
        expected = u"ADM.UNICO: RALUY AYATS JORGE."
        self.assertEqual(expected, result)

    def test_dni_2(self):
        text = u"Adm. Solid.: PELLISE ESQUERDA SANTIAGO. : 40690460X. Adm. Solid.: PELLISE CAPELL JAUME. : 40880652S."
        result = filters.delete_dni(text)
        expected = u"Adm. Solid.: PELLISE ESQUERDA SANTIAGO. Adm. Solid.: PELLISE CAPELL JAUME."
        self.assertEqual(expected, result)

    def test_dni_3(self):
        text = u"Apoderado: ESSLETZBICHLER FRANZ. : Y0821451C."
        result = filters.delete_dni(text)
        expected = u"Apoderado: ESSLETZBICHLER FRANZ."
        self.assertEqual(expected, result)

    def test_dni_4(self):
        text = u"Adm. Unico: DAIAN IOANA. : X9222191L."
        result = filters.delete_dni(text)
        expected = u"Adm. Unico: DAIAN IOANA."
        self.assertEqual(expected, result)

    def test_dni_5(self):
        text = "ADM.UNICO: CORRECT PRAXIS SL. : B64944762. REPR.143 RRM: BLANQUEZ ESPIGARES MIGUEL. : 33882481P."
        result = filters.delete_dni(text)
        expected = "ADM.UNICO: CORRECT PRAXIS SL. REPR.143 RRM: BLANQUEZ ESPIGARES MIGUEL."
        self.assertEqual(expected, result)


class DeleteModificacionDuracion(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_nombramientos(self):
        text = (u"Adm. Unico: GALAN ESPINA MANUEL. Modificación de " +
                u"duración: Indefinida.")
        result = filters.delete_modificacion_duracion(text)
        self.assertEqual(u"Adm. Unico: GALAN ESPINA MANUEL.", result)

    def test_ampliacion_capit_1(self):
        text = (u"Adm. Solid.: GARCIA GIL SERGIO;GARCIA MANCEBON MARIA " +
                u"ENCARNAION. Modificaci\u00f3n de duraci\u00f3n: 31.12.18.")
        result = filters.delete_modificacion_duracion(text)
        self.assertEqual(u"Adm. Solid.: GARCIA GIL SERGIO;GARCIA MANCEBON " +
                         "MARIA ENCARNAION.", result)

    def test_ampliacion_capit_2(self):
        text = (u"Capital: 1.621.846,00 Euros. Resultante Suscrito: " +
                u"3.378.846,00 Euros. Modificaci\u00f3n de duraci\u00f3n: " +
                "TERMINACION DE TRABAJOS,.")
        result = filters.delete_modificacion_duracion(text)
        self.assertEqual(u"Capital: 1.621.846,00 Euros. Resultante Suscrito:" +
                         u" 3.378.846,00 Euros.", result)

    def test_no_text(self):
        text = (u"Capital: 1.621.846,00 Euros. Resultante Suscrito: " +
                u"3.378.846,00 Euros.")
        result = filters.delete_modificacion_duracion(text)
        self.assertEqual(u"Capital: 1.621.846,00 Euros. Resultante Suscrito:" +
                         u" 3.378.846,00 Euros.", result)

if __name__ == "__main__":
    unittest.main()
