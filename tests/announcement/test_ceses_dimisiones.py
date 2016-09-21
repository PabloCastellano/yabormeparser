#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from yabormeparser.announcement import ceses_dimisiones


class TestCesesDimisiones(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # BORME-A-2009-100-49

    def test_cese_0(self):
        c = u"Adm. Solid.: CALVO RIVERA GERMAN;CALVO RIVERA MARIA CARMEN."
        p = ceses_dimisiones.Parser(c)
        self.assertEqual(p.roles[1],
                         (u"ADM. SOLID.", u"CALVO RIVERA MARIA CARMEN"))

    def test_cese_1(self):
        c = u"Adm. Mancom.: LOPEZ CALVO MANUEL;SANCHEZ MARTIN ESTEBAN;IGLESIAS MENDEZ PASCUAL;PEDRERO IGLESIAS JOSE ANTONIO."
        p = ceses_dimisiones.Parser(c)
        self.assertEqual(p.roles[-1],
                         (u"ADM. MANCOM.", u"PEDRERO IGLESIAS JOSE ANTONIO"))

    def test_cese_2(self):
        c = u"Consejero: BRAVO GANADO CARLOS. Presidente: BRAVO GANADO CARLOS. Consejero: MARTIN GARCIA ANTONIO. Vicepresid.: MARTIN GARCIA ANTONIO. Consejero: MATILLA BERMEJO MIGUEL. Secretario: MATILLA BERMEJO MIGUEL."
        p = ceses_dimisiones.Parser(c)
        self.assertEqual(p.roles[-2],
                         (u"CONSEJERO", u"MATILLA BERMEJO MIGUEL"))


    def test_cese_3(self):
        c = u"Adm. Solid.: GARCIA ALFARAZ MAXIMO;MARTIN FRAILE CARLOS."
        p = ceses_dimisiones.Parser(c)
        self.assertEqual(p.roles[1],
                         (u"ADM. SOLID.", u"MARTIN FRAILE CARLOS"))


    def test_cese_4(self):
        c = u"Adm. Solid.: SAN GREGORIO SANTOS CANDIDO."
        p = ceses_dimisiones.Parser(c)
        self.assertEqual(p.roles[0],
                         (u"ADM. SOLID.", u"SAN GREGORIO SANTOS CANDIDO"))

# BORME-A-2013-238-15

    def test_cese_5(self):
        c = u"Adm. Unico: TAP OBRA CIVIL Y EDIFICACION SOCIEDAD LIMITADA."
        p = ceses_dimisiones.Parser(c)
        self.assertEqual(p.roles[0],
                         (u"ADM. UNICO",
                          u"TAP OBRA CIVIL Y EDIFICACION SOCIEDAD LIMITADA"))

    def test_cese_6(self):
        c = u"Adm. Unico: BLANCO RODRIGUEZ JOSE."
        p = ceses_dimisiones.Parser(c)
        self.assertEqual(p.roles[0],
                         (u"ADM. UNICO", u"BLANCO RODRIGUEZ JOSE"))

    def test_cese_7(self):
        c = u"Adm. Solid.: LAGO GARCIA MANUEL;GARCIA MERA XABIER."
        p = ceses_dimisiones.Parser(c)
        self.assertEqual(p.roles[1],
                         (u"ADM. SOLID.", u"GARCIA MERA XABIER"))

    def test_cese_8(self):
        c = u"Adm. Solid.: COUCHEIRO FAILDE JOSE ANTONIO;EXPOSITO ALCOCER JOSE."
        p = ceses_dimisiones.Parser(c)
        self.assertEqual(p.roles[1],
                         (u"ADM. SOLID.", u"EXPOSITO ALCOCER JOSE"))


# BORME-A-2014-199-28

    def test_cese_9(self):
        c = u"Adm. Unico: IC NON RESIDENTS SL. Representan: CABANAS NAVAZO BLANCA PILAR."
        p = ceses_dimisiones.Parser(c)
        self.assertEqual(p.roles[-1],
                         (u"REPRESENTAN", u"CABANAS NAVAZO BLANCA PILAR"))

    def test_cese_10(self):
        c = u"Consejero: ALFONSO MARTINEZ AINHOA;DUPIN LIRZIN CATHERINE;ALFONSO ALFONSO JOSE MIGUEL. Presidente: ALFONSO ALFONSO JOSE MIGUEL. Cons.Del.Sol: ALFONSO ALFONSO JOSE MIGUEL;DUPIN LIRZIN CATHERINE. SecreNoConsj: FUENTES GOMEZ RODRIGO."
        p = ceses_dimisiones.Parser(c)
        self.assertEqual(p.roles[-1],
                         (u"SECRENOCONSJ", u"FUENTES GOMEZ RODRIGO"))


    def test_cese_11(self):
        c = u"Consejero: RIBERA SALUD SA. Presidente: RIBERA SALUD SA. Consejero: RIBERA SALUD PROYECTOS SL;RIBERA SALUD INFRAESTRUCTURAS SL;RIBERA SALUD TECNOLOGIAS SL;TORREVIEJA SALUD SL;INSTITUTO DE GESTION SANITARIA SA;ENTORNO 2000 SA;TENEDORA DE PARTICIPACIONES TECNOLOGICAS SA;ARACIL GALLARDO JOSE;FERNANDEZ VIDAL FERNANDO MANUEL. SecreNoConsj: FERNANDEZ MARTINEZ MARIA."
        p = ceses_dimisiones.Parser(c)
        self.assertEqual(p.roles[3],
                         (u"CONSEJERO", u"RIBERA SALUD INFRAESTRUCTURAS SL"))


    def test_cese_12(self):
        c = u"Consejero: GONZALEZ QUINTANA JUAN JOSE;CORTIJO GIRBAL FRANCISCO;MIRANDA VIÑUELAS LUIS MIGUEL. Presidente: CORTIJO GIRBAL FRANCISCO. Con.Delegado: CORTIJO GIRBAL FRANCISCO."
        p = ceses_dimisiones.Parser(c)
        self.assertEqual(p.roles[-1],
                         (u"CON.DELEGADO", u"CORTIJO GIRBAL FRANCISCO"))


    def test_cese_13(self):
        c = u"Consejero: BUENO GIL LUIS;CERVERA LIZAUR JUAN JOSE;ATIENZA MEDINA PABLO. Presidente: BUENO GIL LUIS. Secretario: CERVERA LIZAUR JUAN JOSE. Cons.Del.Sol: ATIENZA MEDINA PABLO;BUENO GIL LUIS;CERVERA LIZAUR JUAN JOSE."
        p = ceses_dimisiones.Parser(c)
        self.assertEqual(p.roles[4],
                         (u"SECRETARIO", u"CERVERA LIZAUR JUAN JOSE"))

if __name__ == "__main__":
    unittest.main()
