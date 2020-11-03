

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

    def getOneVerse(self, verseNumber):

        if isinstance(verseNumber, int):

            lenXmas = len(self.daysOfXmas)
            if verseNumber >= lenXmas or verseNumber < (-1) * lenXmas:
                raise ValueError("Podaj liczbę z zakresu 0 - 11")

            print(self.daysOfXmas[verseNumber])
            return self.daysOfXmas[verseNumber]
        else:
            raise ValueError

    def getVerses(self, fromVerse, toVerse):
        if isinstance(fromVerse, int) and isinstance(toVerse, int):

            lenXmas = len(self.daysOfXmas)

            leftNumberNotOK = fromVerse >= lenXmas or fromVerse < (-1) * lenXmas
            rightNumberNotOK = toVerse >= lenXmas or toVerse < (-1) * lenXmas

            if leftNumberNotOK or rightNumberNotOK:
                raise ValueError("Podaj liczbę z zakresu 0 - 11")

            verses = []
            for i in range(fromVerse, toVerse, 1):
                verses.append(self.daysOfXmas[i])

            return verses
        else:
            raise ValueError

    def getAllSong(self):
        return self.daysOfXmas


import unittest


class ChristmasTest(unittest.TestCase):
    def setUp(self):
        self.temp = Christmas()

    def test_first_verse(self):
        firstVerse = "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree."
        self.assertEqual(self.temp.getOneVerse(0), firstVerse)

    def test_fifth_verse(self):
        fifthVerse = "On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
        self.assertEqual(self.temp.getOneVerse(4), fifthVerse)

    def test_verses_from_0_to_3(self):
        verseList = [
            "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.",
            "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        ]

        self.assertEqual(self.temp.getVerses(0, 3), verseList)

    def test_all_song(self):
        song = [
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

        self.assertEqual(self.temp.getAllSong(), song)

    def test_one_verse_disallow_not_number(self):
        self.assertRaises(ValueError, self.temp.getOneVerse, "1")

    def test_verses_disallow_not_number_left(self):
        self.assertRaises(ValueError, self.temp.getVerses, "1", 1)

    def test_verses_disallow_not_number_right(self):
        self.assertRaises(ValueError, self.temp.getVerses, 1, "1")

    def test_verses_disallow_not_number_both(self):
        self.assertRaises(ValueError, self.temp.getVerses, "1", "1")

    def test_one_verse_must_give_number_in_range(self):
        self.assertRaises(ValueError, self.temp.getOneVerse, 12)

    def test_verses_must_give_number_in_range_left(self):
        self.assertRaises(ValueError, self.temp.getVerses, 12, 0)

    def test_verses_must_give_number_in_range_right(self):
        self.assertRaises(ValueError, self.temp.getVerses, 0, 12)

    def test_verses_must_give_number_in_range_both(self):
        self.assertRaises(ValueError, self.temp.getVerses, 12, 15)


