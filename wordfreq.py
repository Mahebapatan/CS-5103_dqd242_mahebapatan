"""
 Program:
 Python program to count frequency of each word in a string, the string is passed in program for testing once and then through a text file
"""
import re


def get_word_freq(ip_string): 

   # convert the input string into a list of words
   #input_string_list = re.split('\n|\t| ', input_string)
   #delimiters = " ", "\n", "\t"
   #regex_pattern = '|'.join(map(re.escape, delimiters))
   #regex_pattern
   #input_string_list = re.split(regex_pattern, input_string)
   #input_string_list = input_string.split() 
   input_string_list = ip_string.strip().split()
   #list(map(lambda x:x.strip(),input_string_list))   
   
      #input_string_list1 = input_string_list.split('\n') 
   unique_str_list = [] 

   # iterate the input string list and find unique words 
   for i in input_string_list:         

      # test for duplicate values 
      if i not in unique_str_list: 

         # add unique words to second list
         unique_str_list.append(i) 

   print("*******************")
   print("unique_string_list = ", unique_str_list)
   print("*******************\n")
   
   print("*******************")
   for i in range(0, len(unique_str_list)): 

      # compute word frequency in input string 
      print('Word Frequency [{}]: {}'.format(unique_str_list[i], input_string_list.count(unique_str_list[i])))
    
   print("*******************")

def Driver():
    text = open("sample.txt", "r")
    ip_string = text.read()
    """ python csharp javascript php python javascript csharp python csharp php\tmahi\nmahi please test c,c \
      yes python csharp javascript php python javascript csharp python csharp php\tmahi\nmahi please test c,c \
      yespython csharp javascript php python javascript csharp python csharp php\tmahi\nmahi please test c,c \
      yes python csharp javascript php python javascript csharp python csharp php\tmahi\nmahi please test c,c \
      yes python csharp javascript php python javascript csharp python csharp php\tmahi\nmahi please test c,c \
      yes python csharp javascript php python javascript csharp python csharp php\tmahi\nmahi please test c,c \
      yes python csharp javascript php python javascript csharp python csharp php\tmahi\nmahi please test c,c \
      yes python csharp javascript php python javascript csharp python csharp php\tmahi\nmahi please test c,c \
      yes python csharp javascript php python javascript csharp python csharp php\tmahi\nmahi please test c,c \
      yes python csharp javascript php python javascript csharp python csharp php\tmahi\nmahi please test c,c \
      yes python csharp javascript php python javascript csharp python csharp php\tmahi\nmahi please test c,c \
      yes"""
    print(ip_string) 
    get_word_freq(ip_string)                

if __name__=="__main__": 
   Driver()          # call Driver() function
