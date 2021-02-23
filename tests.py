import unittest

from translator import englishtofrench, englishtogerman

class Test_englishtofrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishtofrench(None), None) # test when the input is None

        self.assertEqual(englishtofrench("Hello"), "Bonjour") # test when the input is the Word "Hello"

        self.assertEqual(englishtofrench("This is a test"), "Il s'agit d'un test") # test when the input is "This is a test"



class Test_englishtogerman(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishtogerman(None), None) # test when the input is None

        self.assertEqual(englishtogerman("Hello"), "Hallo") # test when the input is the Word "Hello"

        self.assertEqual(englishtogerman("This is a test"), "Das ist ein Test") # test when the input is "This is a test"

unittest.main()