from wordfreq import get_word_freq
   # The code to test
import unittest   # The test framework
text = open("sample.txt", "r")
input_string = text.read()
print(input_string)
        

class Test_wordcount(unittest.TestCase): 
       pass      
       def test_one_word(self):
           s = "hello"
           self.assertEqual(get_word_freq(s), get_word_freq(s))
           
       def test_emptystring(self):
           text = open("sample.txt", "r")
           s = text.read()
           self.assertEqual(get_word_freq(s), get_word_freq(s))
           
       def test_string(self):
           s = "hello"
           self.assertEqual(get_word_freq(s), get_word_freq(s))
        
    

if __name__ == '__main__':
    unittest.main()