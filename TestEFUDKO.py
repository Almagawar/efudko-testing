import EFUDKO
import unittest

class TestEFUDKO(unittest.TestCase):

    def setUp(self):
        self.efudko = EFUDKO.Efudko()
        self.efudko.login()

    def tearDown(self):
        self.efudko.close()

    # def test_elem_id(self):
    #     elem_id = self.efudko.elem_id()
    #     self.assertEqual(elem_id, 'homeLink')

    # def test_del_tab(self):
    #     self.efudko.del_tab()

    def test_doc_kit_creation(self):
        self.efudko.doc_kit_creation()

if __name__ == '__main__':
    unittest.main()