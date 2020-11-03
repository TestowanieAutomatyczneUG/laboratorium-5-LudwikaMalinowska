

class Christmas:

    daysOfXmas = [

        "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.",

        "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.",

        "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",

        "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",

        "On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",

        "On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",

        "On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",

        "On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",

        "On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",

        "On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",

        "On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",

        "On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
    ]

    def xmas(self, numberOfVerses, verseNumber):
        if (numberOfVerses == 1):
            return self.daysOfXmas[verseNumber]

    def getVerses(self, fromVerse, toVerse):
        verses = []
        for i in range (fromVerse, toVerse, 1):
            verses.append(self.daysOfXmas[i])

        return verses




import unittest


class ChristmasTest(unittest.TestCase):
    def setUp(self):
        self.temp = Christmas()

    def test_first_verse(self):
        firstVerse = "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree."
        self.assertEqual(self.temp.xmas(1,0), firstVerse)

    def test_fifth_verse(self):
        fifthVerse = "On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
        self.assertEqual(self.temp.xmas(1,4), fifthVerse)

    def test_verses_from_a_to_b(self):
        verseList = [

            "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.",

            "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.",

            "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        ]

        self.assertEqual(self.temp.getVerses(0, 3), verseList)





