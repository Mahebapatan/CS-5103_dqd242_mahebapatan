"""
 Author: Maheba Patan
 Program: Word count
 Python program to count frequency of each word in a string, the string is passed in program for testing once and then through a text file
"""
import re


def get_word_freq(ip_string): 

   input_string_list = ip_string.strip().split()
   unique_str_list = [] 

   # iterate the input string list and find unique words 
   for i in input_string_list:         

      # test for duplicate values 
      if i not in unique_str_list: 

         # add unique words to second list
         unique_str_list.append(i) 

   print("*******************")
   #print("unique_string_list = ", unique_str_list)
   print("*******************\n")
   
   print("*******************")
   if len(unique_str_list) == 0:
      print("The input string is empty")
   for i in range(0, len(unique_str_list)): 

      # compute word frequency in input string 
      print('Word Frequency of [{}]: {}'.format(unique_str_list[i], input_string_list.count(unique_str_list[i])))
      
   print("*******************")
   print("The total number of characters in the input file including spaces is : \n\n", len(ip_string))
   text1 = open("sample.txt", "r")
   lines = len(text1.readlines()) 
   print("The number of lines in the input file is: \n\n", lines)

def Driver():
    text = open("sample.txt", "r")
     
    ip_string = text.read()
        
    get_word_freq(ip_string)
    
    
    
    
               

if __name__=="__main__": 
   Driver()          # call Driver() function
