import unittest

class RomanNumerals:
    def roman(self, n):



        rom = ""
        num = n % 10
        num10 = int((n % 100)/10)
        num100 = int(n/100)
        # print(num100)
        # print("num10 ", num10)

        # for i in range (num10):
        #     rom += "X"

        if num100 == 1:
            rom += "C"
        elif num100 == 2:
            rom += "CC"
        elif num100 == 3:
            rom += "CCC"
        elif num100 == 4:
            rom += "CD"
        elif num100 == 5:
            rom += "D"

        if num10 == 1:
            rom += "X"
        elif num10 == 2:
            rom += "XX"
        elif num10 == 3:
            rom += "XXX"
        elif num10 == 4:
            rom += "XL"
        elif num10 == 5:
            rom += "L"
        elif num10 == 6:
            rom += "LX"
        elif num10 == 7:
            rom += "LXX"
        elif num10 == 8:
            rom += "LXXX"
        elif num10 == 9:
            rom += "XC"

        if num == 1:
            rom += "I"
        elif num == 2:
            rom += "II"
        elif num == 3:
            rom += "III"
        elif num == 4:
            rom += "IV"
        elif num == 5:
            rom += "V"
        elif num == 6:
            rom += "VI"
        elif num == 7:
            rom += "VII"
        elif num == 8:
            rom += "VIII"
        elif num == 9:
            rom += "IX"






        return rom




class RomanNumeralsTest(unittest.TestCase):

    def setUp(self):
        self.temp = RomanNumerals()

    def test_1_is_a_single_i(self):
        self.assertEqual(self.temp.roman(1), "I")

    # @unittest.SkipTest
    def test_2_is_two_i_s(self):
        self.assertEqual(self.temp.roman(2), "II")

    # @unittest.SkipTest
    def test_3_is_three_i_s(self):
        self.assertEqual(self.temp.roman(3), "III")

    # @unittest.SkipTest
    def test_4_being_5_1_is_iv(self):
        self.assertEqual(self.temp.roman(4), "IV")

    # @unittest.SkipTest
    def test_5_is_a_single_v(self):
        self.assertEqual(self.temp.roman(5), "V")

    # @unittest.SkipTest
    def test_6_being_5_1_is_vi(self):
        self.assertEqual(self.temp.roman(6), "VI")

    # @unittest.SkipTest
    def test_9_being_10_1_is_ix(self):
        self.assertEqual(self.temp.roman(9), "IX")

    # @unittest.SkipTest
    def test_20_is_two_x_s(self):
        self.assertEqual(self.temp.roman(27), "XXVII")

    # @unittest.SkipTest
    def test_48_is_not_50_2_but_rather_40_8(self):
        self.assertEqual(self.temp.roman(48), "XLVIII")

    # @unittest.SkipTest
    def test_49_is_not_40_5_4_but_rather_50_10_10_1(self):
        self.assertEqual(self.temp.roman(49), "XLIX")

    # @unittest.SkipTest
    def test_50_is_a_single_l(self):
        self.assertEqual(self.temp.roman(59), "LIX")

    # @unittest.SkipTest
    def test_90_being_100_10_is_xc(self):
        self.assertEqual(self.temp.roman(93), "XCIII")

    # @unittest.SkipTest
    def test_100_is_a_single_c(self):
        self.assertEqual(self.temp.roman(141), "CXLI")

    # @unittest.SkipTest
    def test_60_being_50_10_is_lx(self):
        self.assertEqual(self.temp.roman(163), "CLXIII")

    # @unittest.SkipTest
    def test_400_being_500_100_is_cd(self):
        self.assertEqual(self.temp.roman(402), "CDII")

    # @unittest.SkipTest
    def test_500_is_a_single_d(self):
        self.assertEqual(self.temp.roman(575), "DLXXV")

    # @unittest.SkipTest
    def test_900_being_1000_100_is_cm(self):
        self.assertEqual(self.temp.roman(911), "CMXI")

    @unittest.SkipTest
    def test_1000_is_a_single_m(self):
        self.assertEqual(roman(1024), "MXXIV")

    @unittest.SkipTest
    def test_3000_is_three_m_s(self):
        self.assertEqual(roman(3000), "MMM")