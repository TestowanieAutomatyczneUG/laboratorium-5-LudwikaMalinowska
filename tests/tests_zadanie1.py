import unittest

class HammingTest(unittest.TestCase):

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
            # self.temp = Hamming()
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def test_empty_strands(self):
        self.assertEqual(self.distance("", ""), 0)

    @unittest.SkipTest
    def test_single_letter_identical_strands(self):
        self.assertEqual(self.distance("A", "A"), 0)

    @unittest.SkipTest
    def test_single_letter_different_strands(self):
        self.assertEqual(self.distance("G", "T"), 1)

    @unittest.SkipTest
    def test_long_identical_strands(self):
        self.assertEqual(self.distance("GGACTGAAATCTG", "GGACTGAAATCTG"), 0)

    @unittest.SkipTest
    def test_long_different_strands(self):
        self.assertEqual(self.distance("GGACGGATTCTG", "AGGACGGATTCT"), 9)

    @unittest.SkipTest
    def test_disallow_first_strand_longer(self):
        with self.assertRaisesWithMessage(ValueError):
            self.distance("AATG", "AAA")

    @unittest.SkipTest
    def test_disallow_second_strand_longer(self):
        with self.assertRaisesWithMessage(ValueError):
            self.distance("ATA", "AGTG")

    @unittest.SkipTest
    def test_disallow_left_empty_strand(self):
        with self.assertRaisesWithMessage(ValueError):
            self.distance("", "G")

    @unittest.SkipTest
    def test_disallow_right_empty_strand(self):
        with self.assertRaisesWithMessage(ValueError):
            self.distance("G", "")

    @unittest.SkipTest
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")

    def tearDown(self):
        self.temp = None


