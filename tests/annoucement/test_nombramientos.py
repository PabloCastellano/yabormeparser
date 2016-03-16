#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from yabormeparser.annoucement import nombramientos


# BORME-A-2009-100-49


class TestNombramientos2009(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_2009_0(self):
        n = u"Adm. Unico: CALVO RIVERA GERMAN."
        p = nombramientos.Parser(n)
        self.assertEqual(p.roles[0], (u"ADM. UNICO", u"CALVO RIVERA GERMAN"))

    def test_2009_1(self):
        n = u"Apo.Man.Soli: ARIZA LUCAS MARIA ANGELES."
        p = nombramientos.Parser(n)

    def test_2009_2(self):
        n = u"Adm. Mancom.: SANCHEZ MARTIN ESTEBAN;IGLESIAS MENDEZ PASCUAL;PEDRERO IGLESIAS JOSE ANTONIO."
        p = nombramientos.Parser(n)
        self.assertEqual(len(p.roles), 3)
        self.assertEqual(p.roles[2], (u"ADM. MANCOM.",
                                      u"PEDRERO IGLESIAS JOSE ANTONIO"))

    def test_2009_3(self):
        n = u"Consejero: BRAVO GANADO CARLOS. Presidente: BRAVO GANADO CARLOS. Consejero: MARTIN GARCIA ANTONIO. Vicepresid.: MARTIN GARCIA ANTONIO. Consejero: MATILLA BERMEJO MIGUEL. Secretario: MATILLA BERMEJO MIGUEL."
        p = nombramientos.Parser(n)
        self.assertEqual(len(p.roles), 6)
        self.assertEqual(p.roles[3], (u"VICEPRESID.",
                                      u"MARTIN GARCIA ANTONIO"))

    def test_2009_4(self):
        n = u"Adm. Unico: FERRERAS ANDRES MARIA CARMEN."
        p = nombramientos.Parser(n)

    def test_2009_5(self):
        n = u"Adm. Solid.: SAN GREGORIO GALAN ALFONSO;SAN GREGORIO GUTIERREZ ANTONIO."
        p = nombramientos.Parser(n)

    def test_2009_6(self):
        n = u"Adm. Unico: GARCIA ALFARAZ MAXIMO."
        p = nombramientos.Parser(n)
        self.assertEqual(len(p.roles), 1)
        self.assertEqual(p.roles[0], (u"ADM. UNICO", u"GARCIA ALFARAZ MAXIMO"))

    def test_2009_7(self):
        n = u"Cons.Del.Man: ALVARADO SAMPAYO RAUL;SOUTO FERNANDEZ GABINO;FORMOSO FERNANDEZ ANTONIO;FERNANDEZ PROL SERVANDO."
        p = nombramientos.Parser(n)
        self.assertEqual(len(p.roles), 4)

# BORME-A-2014-199-28


class TestNombramientos2014(unittest.TestCase):
    n = ""
    p = nombramientos.Parser(n)
    def test_2014_0(self):
        n = "Adm. Unico: LOPEZ DE LA TORRE VAZQUEZ CARLOS FELIPE."
        p = nombramientos.Parser(n)

    def test_2014_1(self):
        n = "Apo.Manc.: GONZALEZ MOLINA PASUCAL;ECHAVARRI MACON FRANCISCO JAVIER."
        p = nombramientos.Parser(n)
        self.assertEqual(len(p.roles), 2)
        self.assertEqual(p.roles[1], (u"APOD. MANCOM.",
                              u"ECHAVARRI MACON FRANCISCO JAVIER"))

    def test_2014_2(self):
        n = "Auditor: DELOITTE SL."
        p = nombramientos.Parser(n)
        self.assertEqual(len(p.roles), 1)
        self.assertEqual(p.roles[0], (u"AUDITOR", u"DELOITTE SL"))

    def test_2014_3(self):
        n = "Adm. Mancom.: ANDPRIVATE CONSULTING SL;AKM GESTION INMOBILIARIA X SL. Representan: ESTEVEZ OLLEROS FERNANDO HONORINO;GONZALEZ DOLZ XAVIER. Apoderado: ESTEVEZ OLLEROS FERNANDO HONORINO;GONZALEZ DOLZ XAVIER. Auditor: KPMG AUDITORES SL."
        p = nombramientos.Parser(n)
        self.assertEqual(len(p.roles), 7)

    def test_2014_4(self):
        n = "Vicepresid.: RODRIGUEZ GONZALEZ DEMETRIO. Secretario: DE LA ROSA ESCARDA MARCELINO."
        p = nombramientos.Parser(n)

    def test_2014_5(self):
        n = "Consejero: CORPORACION SELIGRAT XXI SL;SELIGRAT ALONSO MARIA TRINIDAD;SELIGRAT SIERRA ENRIQUE;SELIGRAT TORIBIO JOSE RAMON. Secretario: SELIGRAT ALONSO MARIA TRINIDAD. Presidente: CORPORACION SELIGRAT XXI SL. Cons.Del.Man: SELIGRAT ALONSO MARIA TRINIDAD;CORPORACION SELIGRAT XXI SL;SELIGRAT SIERRA ENRIQUE;SELIGRAT TORIBIO JOSE RAMON. Representan: SELIGRAT ALONSO ENRIQUE. Vicesecret.: SELIGRAT TORIBIO JOSE RAMON. Vicepresid.: SELIGRAT SIERRA ENRIQUE."
        p = nombramientos.Parser(n)

    def test_2014_6(self):
        n = "Adm. Mancom.: ECHANIZ URCELAY ALVARO;BARCELO BIOSCA JORGE;PEINADO ALVAREZ JOSE VICENTE."
        p = nombramientos.Parser(n)

    def test_2014_7(self):
        n = "Adm. Unico: REDONDO JIMENEZ LUIS."
        p = nombramientos.Parser(n)

    def test_2014_8(self):
        n = u"Apo.Sol.: BARGE ALVAREZ MIGUEL;BUENO TENA MIGUEL;MARTINEZ GIL MARIA ISABEL;VAL JIMENEZ MARTA;VILLANUEVA LIÑAN JORGE."
        p = nombramientos.Parser(n)

    def test_2014_9(self):
        n = "Liquidador: RAMOS CARRO FRANCISCO JAVIER."
        p = nombramientos.Parser(n)

    def test_2014_10(self):
        n = "Adm. Unico: WU SHENGWEI."
        p = nombramientos.Parser(n)

    def test_2014_11(self):
        n = "Adm. Unico: ASAD AHMED MOHAMMAD BEN ALI."
        p = nombramientos.Parser(n)

    def test_2014_12(self):
        n = "Representan: GUTIERREZ ACEBRON RAUL. Adm. Unico: CONSTRUCCIONES MEGINA SL."
        p = nombramientos.Parser(n)

    def test_2014_13(self):
        n = "R.L.C.Perma.: SETBON PHILIPPE."
        p = nombramientos.Parser(n)

    def test_2014_14(self):
        n = "Consejero: BARTOLOME SANZ MARIA VICTORIA;BARTOLOME SANZ SONIA;BARTOLOME SANZ EUGENIO;BARTOLOME SANZ MARIA JOSE;BARTOLOME SANZ MARIA ELENA;BARTOLOME SANZ GINES. Presidente: BARTOLOME SANZ EUGENIO. Secretario: BARTOLOME SANZ MARIA VICTORIA. Cons.Del.Man: BARTOLOME SANZ MARIA VICTORIA;BARTOLOME SANZ SONIA;BARTOLOME SANZ EUGENIO;BARTOLOME SANZ MARIA JOSE;BARTOLOME SANZ MARIA ELENA;BARTOLOME SANZ GINES."
        p = nombramientos.Parser(n)
        self.assertEqual(len(p.roles), 14)
        self.assertEqual(p.roles[9], (u"CONS.DEL.MAN", u"BARTOLOME SANZ SONIA"))

    def test_2014_15(self):
        n = "Ent. Gestora: BBVA ASSET MANAGEMENT SA SGIIC. Apoderado: BBVA ASSET MANAGEMENT SA SGIIC;BBVA ASSET MANAGEMENT SA SGIIC."
        p = nombramientos.Parser(n)
        self.assertEqual(len(p.roles), 3)
        self.assertEqual(p.roles[2], (u"APODERADO", u"BBVA ASSET MANAGEMENT SA SGIIC"))

    def test_2014_16(self):
        n = "Adm. Unico: LIN XIAOZHEN."
        p = nombramientos.Parser(n)
        self.assertEqual(len(p.roles), 1)
        self.assertEqual(p.roles[0], (u"ADM. UNICO", u"LIN XIAOZHEN"))

    def test_fail_0(self):
        # BORME-A-2009-101-28
        n = "Ger.Com.Ger: SANZ ARNAL ERNESTO."
        p = nombramientos.Parser(n)
        self.assertEqual(len(p.roles), 1)
        self.assertEqual(p.roles[0], (u"GER.COM.GER", u"SANZ ARNAL ERNESTO"))

    def test_fail_1(self):
        # BORME-A-2009-101-28
        n = "Dir. General: PEREZ PEREA FRANCISCO JAVIER. Apoderado: PEREZ PEREA FRANCISCO JAVIER."
        p = nombramientos.Parser(n)
        self.assertEqual(len(p.roles), 2)
        self.assertEqual(p.roles[0], (u"DIR. GENERAL", u"PEREZ PEREA FRANCISCO JAVIER"))

    def test_fail_2(self):
        # BORME-A-2009-101-28
        n = "R.C.P.SolMan: DIEZ RODRIGUEZ IGNACIO. Apo.Manc.: SAINZ DE LA CUESTA ABBAD ALMUDENA;SOTTOMAYOR FRANCISCO."
        p = nombramientos.Parser(n)
        self.assertEqual(len(p.roles), 3)
        self.assertEqual(p.roles[0], (u"R.C.P.SOLMAN", u"DIEZ RODRIGUEZ IGNACIO"))

    def test_fail_3(self):
        # BORME-A-2014-199-17
        n = "Adm. Unico: JORDI BELL.LLOCH CORNEY."
        p = nombramientos.Parser(n)
        self.assertEqual(len(p.roles), 1)
        self.assertEqual(p.roles[0], (u"ADM. UNICO", u"JORDI BELL.LLOCH CORNEY"))

    def no_test_fail_4(self):
        n = "Consejero: DAMIA ALBERT JUAN JOSE;RAMIA FABREGAT FRANCISCO-JAVIER;TUROL DIVERSIA SL;AGROTAULA SL;COOPERATIVA AGRICOLA BENASALENSE COOP. V.;SELCO MANAGEMENT CONSULTANTS SL.Presidente: AGROTAULA SL. Secretario: DAMIA ALBERT JUAN JOSE."
        p = nombramientos.Parser(n)
        self.assertEqual(len(p.roles), 8)
        self.assertEqual(p.roles[4], (u"CONSEJERO", u"COOPERATIVA AGRICOLA BENASALENSE COOP. V."))

    def test_fail_5(self):
        n = "Miem.Com.Liq: MARTINEZ TEJERO MARIA JESUS;REDONDO PEREZ ANTONIO;VALDERRAMA CONDE JAIME;ALVAREZ SAENZ CESAR."
        p = nombramientos.Parser(n)
        self.assertEqual(len(p.roles), 4)
        self.assertEqual(p.roles[3], (u"MIEM.COM.LIQ", u"ALVAREZ SAENZ CESAR"))

    def test_fail_6(self):
        """It tests case no sensitive"""
        n = "LIQUIDADOR: CAPARROS LOPEZ FRANCISCO."
        p = nombramientos.Parser(n)
        self.assertEqual(len(p.roles), 1)
        self.assertEqual(p.roles[0], (u"LIQUIDADOR", u"CAPARROS LOPEZ FRANCISCO"))

    def test_space_with_hyphen(self):
        """It tests when the hyphen is in the end line and add a space"""
        n = "V- SEC.COMS.E: CAPARROS LOPEZ FRANCISCO."
        p = nombramientos.Parser(n)
        self.assertEqual(len(p.roles), 1)
        self.assertEqual(p.roles[0], (u"V-SEC.COMS.E", u"CAPARROS LOPEZ FRANCISCO"))

if __name__ == "__main__":
    unittest.main()
