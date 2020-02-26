import EFUDKO
import unittest

class TestEFUDKO(unittest.TestCase):

    def setUp(self):
        self.efudko = EFUDKO.Efudko()
        self.efudko.boot()

    def tearDown(self):
        self.efudko.close()

    def test_doc_kit_creation(self):
        self.efudko.doc_kit_creation("efdmanagerca", "2wsx2WSX")

    def test_del_and_restore(self):
        self.efudko.del_and_restore()

if __name__ == '__main__':
    unittest.main()