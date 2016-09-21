#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from yabormeparser import parser
import os


class TestFileExampleA(unittest.TestCase):

    def setUp(self):
        file_ = 'examples/BORME-A-2013-238-15.pdf'
        self.docparser = parser.Parser(file_)
        self.doc = self.docparser.document

    def tearDown(self):
        file_ = './test_json.json'
        if os.path.isfile(file_):
            os.remove(file_)

    def test_borme_metadata(self):
        doc = self.doc
        self.assertEqual(len(doc['pages']), 2)
        title = u'Actos de A CORUÑA del BORME núm. 238 de 2013'
        self.assertEqual(doc['title'], title)
        self.assertEqual(doc['subject'], 'BORME-A-2013-238-15')

    def test_borme_content_length(self):
        doc = self.doc
        self.assertEqual(len(doc['pages']), 2)
        self.assertEqual(len(doc['pages'][0]), 9)
        self.assertEqual(len(doc['pages'][1]), 2)

    def test_borme_title_acts(self):
        self._assert_title(0, 0, '532404', 'SIGUEME, GESTION Y SERVICIOS SL',
                           'R.M. SANTIAGO DE COMPOSTELA')
        self._assert_title(0, 8, '532412',
                           u'PISTA CATRO PRODUCTORA DE SOÑOS SL',
                           u'R.M. SANTIAGO DE COMPOSTELA')
        self._assert_title(1, 0,
                           '532413', u'PISTA CATRO PRODUCTORA DE SOÑOS SL',
                           'R.M. SANTIAGO DE COMPOSTELA')
        self._assert_title(1, 1,
                           '532414', 'VILLAVERDE Y BOTANA SL',
                           'R.M. SANTIAGO DE COMPOSTELA')

    def test_borme_act_labels(self):
        self._assert_announcement_label(0, 0, 0, u'Ceses/Dimisiones')
        self._assert_announcement_label(0, 8, 1, u'Nombramientos')
        self._assert_announcement_label(1, 0, 3, u'Cambio de domicilio social')
        self._assert_announcement_label(1, 1, 0, u'Constitución')

    def test_borme_act_values(self):
        self._assert_announcement_value(0, 0, 0, u'Adm. Unico: TAP OBRA CIVIL' +
                                       u' Y EDIFICACION SOCIEDAD LIMITADA.')
        self._assert_announcement_value(0, 8, 1, 'Adm. Solid.: COUCHEIRO ' +
                                       'FAILDE JOSE ANTONIO;EXPOSITO ' +
                                       'ALCOCER JOSE.')
        self._assert_announcement_value(1, 0, 3, 'C/ DE LAS CANCELAS 125 ' +
                                       '(SANTIAGO DE COMPOSTELA).')
        self._assert_announcement_value(1, 1, 3, u'T 211 , F 146, S 8, H SC ' +
                                       u'46962, I/A 1 ( 5.12.13).')

    def test_json_file_save(self):
        json_file = open('./test_json.json', "w+")
        self.docparser.save_result(json_file)
        json_file.close()
        json_file2 = open('./test_json.json', "r")
        other = parser.Parser()
        other.load_json(json_file2)
        json_file.close()
        self.assertEqual(self.doc, other.document)

    def test_file_without_announcements_2013(self):
        json_file = open('examples/BORME-A-2013-238-15.RAW.json', "r")
        other = parser.Parser()
        other.load_json(json_file)
        json_file.close()
        self.assertEqual(self._delete_announcements(self.doc),
                         self._delete_announcements(other.document))

    def test_file_with_announcement_labels_2013(self):
        json_file = open('examples/BORME-A-2013-238-15.RAW.json', "r")
        other = parser.Parser()
        other.load_json(json_file)
        json_file.close()
        self.assertEqual(self._delete_announcements_but_labels(self.doc),
                         self._delete_announcements_but_labels(other.document))

    def test_file_with_announcement_2013(self):
        json_file = open('examples/BORME-A-2013-238-15.RAW.json', "r")
        other = parser.Parser()
        other.load_json(json_file)
        json_file.close()
        self.assertEqual(self.doc, other.document)

    def _assert_title(self, page_num, act_num, code, company, register):
        act = self.doc['pages'][page_num][act_num]
        self.assertEqual(act['code'], code)
        self.assertEqual(act['company'], company)
        self.assertEqual(act['register'], register)

    def _assert_announcement_label(self, page_num, act_num, ann_num, label):
        act = self.doc['pages'][page_num][act_num]
        ann = act['announcements'][ann_num]
        self.assertEqual(ann['label'], label)

    def _assert_announcement_value(self, page_num, act_num, ann_num, value):
        act = self.doc['pages'][page_num][act_num]
        ann = act['announcements'][ann_num]
        self.assertEqual(ann['value'], value)

    def _delete_announcements(self, doc):
        for page in doc["pages"]:
            for act in page:
                act["announcements"] = []
        return doc

    def _delete_announcements_but_labels(self, doc):
        for page in doc["pages"]:
            for act in page:
                for ann in act["announcements"]:
                    trash = []
                    for key in ann:
                        if not key == "label":
                            trash.append(key)
                    for key in trash:
                        ann.pop(key)
        return doc

if __name__ == '__main__':
    unittest.main()
