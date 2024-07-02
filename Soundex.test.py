import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")

    def test_encode_name(self):
        self.assertEqual(encode_name("Amrutha","A",0),"A563")

    def test_adjacent_letter(self):
        self.assertEqual(generate_soundex("Aamrutha"),"A563")

    def test_letter_associated_same_number(self):
        self.assertEqual(generate_soundex("adtmrutha"),"A356")

    def test_encode_name_vowels_only(self):
        self.assertEqual(encode_name("aeiou","A",0),"A000")

    def test_only_special_character(self):
        self.assertEqual(encode_name("@&%",'@',0),"@000")

     def test_mixed_chars(self):
        self.assertEqual(generate_soundex("Tom&Jerry"), "T526") 
        




        

    
if __name__ == '__main__':
    unittest.main()
