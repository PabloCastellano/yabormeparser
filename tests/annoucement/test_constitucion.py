#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import yabormeparser.annoucement.constitucion as constitucion

class TestConstitucion(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_2014_0(self):
        c = u"Comienzo de operaciones: 22.09.14. Objeto social: COMPRA, VENTA, PROMOCION Y EXPLOTACION DE TODA CLASE DE BIENES INMUEBLES. PROMOCION O FOMENTO DE EMPRESAS MEDIANTE PARTICIPACION TEMPORAL EN SU CAPITAL Y REALIZACION DE LAS OPERACIONES DE SUSCRIPCION DE ACCIONES O PARTICIPACIONES DE SOCIEDADES DEDICADAS A ACTIVIDADES DE CARACTER EMPRESARIAL, ... Domicilio: PASEO DEL PINTOR ROSALES, 32, 1º (MADRID). Capital: 337.500,00 Euros."
        p = constitucion.Parser(c)
        self.assertEqual(p.begin, u"2014-09-22")
        self.assertEqual(p.purpose[:10], u"COMPRA, VE"[:10])
        self.assertEqual(p.address, u"PASEO DEL PINTOR ROSALES, 32, 1º (MADRID).")
        self.assertEqual(p.capital, 337500.0)

    def test_2014_1(self):
        c = u"Comienzo de operaciones: 22.09.14. Objeto social: MANIPULACION DE TODA CLASE DE PAPEL, CARTON, CARTULINA O MATERIALES SIMILARES. FABRICACION DE SACOS, BOLSAS, CAJAS, SU DISTRIBUCION, VENTA, IMPORTACIO'N, EXPORTACION Y COMERCIALIZACION EN TODOS SUS ASPECTOS... Domicilio: C/ PINTO, 70 (PARLA). Capital: 112.500,00 Euros."
        p = constitucion.Parser(c)
        self.assertEqual(p.begin, u"2014-09-22")
        self.assertEqual(p.purpose[:10], u"MANIPULACI"[:10])
        self.assertEqual(p.address, u"C/ PINTO, 70 (PARLA).")
        self.assertEqual(p.capital, 112500.0)

    def test_2014_2(self):
        c = u"Comienzo de operaciones: 8.08.14. Objeto social: a).- Compraventa de bienes inmobiliaria por cuenta propia (siendo esta su actividad principal CNAE 6810). b).- La compra y venta por cuenta propia o ajena de toda clase de fincas rústicas y rubanas, su explotación directa o indirectamente; la promoción, urbanización, parcelación, reparcelación, .. Domicilio: PASEO DE LA HABANA 9-11 - BAJO (MADRID). Capital suscrito: 60.101,00 Euros. Desembolsado: 60.101,00 Euros."
        p = constitucion.Parser(c)
        self.assertEqual(p.begin, u"2014-08-08")
        self.assertEqual(p.purpose[:10], u"a).- Comprav"[:10])
        self.assertEqual(p.address, u"PASEO DE LA HABANA 9-11 - BAJO (MADRID).")
        self.assertEqual(p.capital, 60101.0)

    def test_2014_3(self):
        c = u"Comienzo de operaciones: 2.10.14. Objeto social: La venta en régimen de concesionario de toda clase de vehículos. La compraventa de vehículos usados. La reparación de vehículos, incluso de carrocería. La venta de accesorios y piezas de recambio para dichos vehículos, y en general cuanto se relaciona con la venta de vehículos nuevos... Domicilio: CTRA DE MADRID COLMENAR VIEJO - KM 28.4 (COLMENAR VIEJO). Capital: 3.006,00 Euros."
        p = constitucion.Parser(c)
        self.assertEqual(p.begin, u"2014-10-02")
        self.assertEqual(p.purpose[:10], u"La venta en régimen"[:10])
        addr = u"CTRA DE MADRID COLMENAR VIEJO - KM 28.4 (COLMENAR VIEJO)."
        self.assertEqual(p.address, addr)
        self.assertEqual(p.capital, 3006.0)

    def test_2014_4(self):
        c = u"Comienzo de operaciones: 25.09.14. Objeto social: - Venta de equipos, herramientas e instalaciones para la industria. - Consulting en marketing comercial multisectorial y marketing online. Si las disposiciones legales exigieran, para el ejercicio de alguna de las actividades enumeradas y comprendidas en el objeto social, algún título profesional, a. Domicilio: C/ DOLORES BARRANCO 57 (MADRID). Capital: 3.100,00 Euros."
        p = constitucion.Parser(c)
        self.assertEqual(p.begin, u"2014-09-25")
        self.assertEqual(p.purpose[:10], u"- Venta de equipos,"[:10])
        self.assertEqual(p.address, u"C/ DOLORES BARRANCO 57 (MADRID).")
        self.assertEqual(p.capital, 3100.0)

    def test_2009_0(self):
        c = u"Comienzo de operaciones: 27.03.09. Duración: 27.03.13. Objeto social: EL SERVICIO DE GESTION PARA EL PAGO DE NOMINAS DE LOS EXCEDENTES LABORALESDERIVADOS DEL PLAN NACIONAL DE RESERVA ESTRATEGICA DE CARBON 2006-2012 EN MATERIA DE PREJUBILACIONES. Domicilio: AVDA DE BURGOS 109 (MADRID). Capital: 5.000,00 Euros."
        p = constitucion.Parser(c)
        self.assertEqual(p.begin, u"2009-03-27")
        self.assertEqual(p.purpose[:10], u"EL SERVICIO DE GESTION PARA EL PAGO DE"[:10])
        self.assertEqual(p.address, u"AVDA DE BURGOS 109 (MADRID).")
        self.assertEqual(p.capital, 5000.0)

    def test_2009_1(self):
        c = u"Comienzo de operaciones: 1.04.09. Objeto social: LA SUSCRIPCION, COMPRAVENTA O TENENCIA DE ACCIONES O PARTICIPACIONES DE SOCIEDADES, TITULOS DE RENTA FIJA Y CUALESQUIERA OTROS DE ANALOGA NATURALEZA,YA SEA A NIVEL PARTICULAR O MEDIANTE LA PARTICIPACION EN INSTITUCIONES DE INVERSION COLECTIVA.. Domicilio: C/ ENRIQUE GRANADOS 6 - EDIFICIO B, COMPLEJO EMPR (POZUELO DE ALARCON). Capital: 3.200.000,00 Euros."
        p = constitucion.Parser(c)
        self.assertEqual(p.begin, u"2009-04-01")
        self.assertEqual(p.purpose[:10], u"LA SUSCRIPCION, COMPRAV"[:10])
        self.assertEqual(p.address, (u"C/ ENRIQUE GRANADOS 6 - EDIFICIO B, COMPLEJO" +
                             u" EMPR (POZUELO DE ALARCON)."))
        self.assertEqual(p.capital, 3200000.0)

    def test_2009_2(self):
        c = u"Comienzo de operaciones: 13.05.09. Objeto social: COMERCIO AL POR MENOR DE ARTICULOS DE REGALO, COMPLEMENTOS DE MODA Y DECORACION.Domicilio: C/ CIUDAD REAL 10 (GUADARRAMA). Capital: 3.006,00 Euros."
        p = constitucion.Parser(c)
        self.assertEqual(p.begin, u"2009-05-13")
        self.assertEqual(p.purpose[:10], u"COMERCIO AL POR MENOR"[:10])
        self.assertEqual(p.address, u"C/ CIUDAD REAL 10 (GUADARRAMA).")
        self.assertEqual(p.capital, 3006.0)

    def test_2009_3(self):
        c = u"Comienzo de operaciones: 4.05.09. Objeto social: LA REALIZACION DE TODA CLASE DE PROSPECCIONES Y EXCAVACIONES ARQUEOLOGICASEN GENERAL Y EN PARTICULAR, OBRAS Y PROYECTOS DE RESTAURACION, CONSERVACION Y REVALORIZACION. Domicilio: PASEO DE LAS DELICIAS NUMERO 11 PISO 3º A (MADRID). Capital: 3.006,00 Euros."
        p = constitucion.Parser(c)
        self.assertEqual(p.begin, u"2009-05-04")
        self.assertEqual(p.purpose[:10], u"LA REALIZACION DE TODA"[:10])
        self.assertEqual(p.address, (u"PASEO DE LAS DELICIAS NUMERO 11 PISO 3º A" +
                                     " (MADRID)."))
        self.assertEqual(p.capital, 3006.0)

    def test_2009_100_3(self):
        """Non-ASCII character in date"""
        c = u"Comienzo de operaciones: 6.04.09º. Objeto social: PRODUCCION Y DISTRIBUCION DE PRODUCTOS Y PRESTACIONES DE SERVICIOS EN LA FASE PREVIA DE LA IMPRESION INCLUSIVE EL DISEÑO, GESTION DE COLORES, DATOS YFLUJOGRAMAS ASI COMO LA GESTION DE LA PRODUCCION DE PRODUCTOS DE IMPRESORAS. Domicilio: C/ TOMAS EDISON, 4 EDIFICIO 1, LOFT 1428 (RIVAS-VACIAMADRID). Capital: 3.006,00 Euros."
        p = constitucion.Parser(c)
        self.assertEqual(p.begin, u"2009-04-06")
        self.assertEqual(p.capital, 3006.0)

    def test_complex_date_0(self):
        """Date with a strange string after 01.02.12."""
        c = u"Comienzo de operaciones: 19.11.1319/11/2013. Objeto social: Explotaci\u00f3n de fincas agrarias y explotaciones ganaderas. Arrendamiento no financiero de fincas agrarias, arrendamiento no financiero de explotaciones ganaderas y arrendamiento no financiero de inmuebles. Compraventa de fincas r\u00fasticas y explotaciones ganaderas. Realizaci\u00f3n de trabajos accesorios de. Domicilio: C/ BUCHARABOLA 1 (AZARA). Capital: 10.000,00 Euros."
        p = constitucion.Parser(c)
        self.assertEqual(p.begin, u"2013-11-19")
        self.assertEqual(p.purpose[:10], u"Explotaci\u00f3n de fincas agrarias"[:10])
        self.assertEqual(p.capital, 10000.0)


    def test_alphabetical_start_date(self):
        """Alphabetical date in start date."""
        c = u"Comienzo de operaciones: DIA ALTA I.A.E. Objeto social: LOS SERVICIOS,ASESORAMIENTO Y CONSULTING DE PROYECTOS DE INGENIERIA Y OFICINA TECNICA. Domicilio: CL COVADONGA Num.359 P.4 PTA.6 (SABADELL). Capital: 3.006,00 Euros."
        p = constitucion.Parser(c)
        # self.assertEqual(p.begin, u"2013-11-19")
        self.assertEqual(p.purpose[:10], u"LOS SERVICIOS,ASESORAMIENTO Y"[:10])
        self.assertEqual(p.capital, 3006.0)

    def test_alphabetical_duration_date(self):
        """Alphabetical date in duration."""
        c = u"Comienzo de operaciones: 24.07.08. Duraci\u00f3n: FIN OBRA. Objeto social: EJECUCION DE LAS OBRAS: PROJECTO OBRA MUNICIPAL ORDINARIA DE LA PLAZA CASABLANCA PREVISTO EN EL PLAN DE MEJORA INTEGRAL AL BARRIO DE CASABLANCA DE SANT BOI DE LLOBREGAT. Domicilio: CL GRAN VIA DE L'HOSPITALET 16 AL 20 (HOSPITALET DE LLOBREGAT (L'). Capital: 6.000,00 Euros."
        p = constitucion.Parser(c)
        self.assertEqual(p.begin, u"2008-07-24")
        self.assertEqual(p.length, u"0000-00-00")
        self.assertEqual(p.purpose[:10], u"EJECUCION DE LAS OBRAS"[:10])
        self.assertEqual(p.capital, 6000.0)

    def test_error_in_date_format(self):
        """Alphabetical date in duration."""
        c = u"Comienzo de operaciones: 23.03.09. Domicilio: CALLE CUATRO ESQUINAS, NUMERO 2-1\u00ba, OFICINA 4,TAFA (TAFALLA). Capital: 100.000,00 Euros."
        p = constitucion.Parser(c)
        self.assertEqual(p.begin, u"2009-03-23")
        self.assertEqual(p.capital, 100000.0)

    def test_error_in_date_alphabetical_format(self):
        """ The date is alphabetical garbage but starts with a number"""
        c = u"Comienzo de operaciones: INSCRIPCION REGISTRO CNMV. Duraci\u00f3n: 10 A\u00d1OS. Objeto social: TOMA DE PARTICIPACIONES TEMPORALES EN EL CAPITAL DE EMPRESAS NO FINANCIERASY DE NATURALEZA NO INMOBILIARIA QUE EN EL MOMENTO DE LA TOMA DE PARTICIPACIONES,NO COTICEN EN EL PRIMER MERCADO DE BOLSAS DE VALORES,ETC. Domicilio: CL DELS CAVALLERS Num.50 (BARCELONA). Capital suscrito: 1.200.800,00 Euros. Desembolsado: 1.200.800,00 Euros."
        p = constitucion.Parser(c)
        self.assertEqual(p.length, u"0000-00-00")
        self.assertEqual(p.capital, 1200800.0)

if __name__ == '__main__':
    unittest.main()
