import unittest

class TestDemoServer(unittest.TestCase):
    def setUp(self):
        pass
    def testCase1(self):
        self.assertEqual(True, True, 'test failed!')
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()