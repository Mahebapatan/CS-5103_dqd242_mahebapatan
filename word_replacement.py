"""
   Author: Maheba Patan
   Program: Word replacement 
   Python program to replace all the occurences of a given word in a text file with the replacement word 
"""
import re


def get_word_replacement(ip_string): 

    if len(ip_string) == 0:
       print("The input string is empty")
    else:   
       # Accept the input from the user for the given word and the replacement word
       old_word = input("Provide the old word to be replaced :")
       new_word = input("Provide the new word to be replaced with :")
       
       if len(old_word) == 0:
          print("the word is not passed it's spaces. please start again ")
       else:
       
          # Replace all occurrences of old word with the new word 
          replaced   = re.sub(r'(?<!\S)' + re.escape(old_word) + r'(?!\S)', new_word, ip_string)  
        
          # Write the modified contents to the file
          if (ip_string == replaced):
             print("Nothing changed becuase word not found")
          with open('sample1.txt', 'w') as file:
               file.write(replaced)
               print("modified/replaced text file contents : ", replaced) 
   

def Driver():   
    text = open("sample1.txt", "r")     
    ip_string = text.read()
    print("input string is:  ", ip_string)
    get_word_replacement(ip_string)
    
if __name__=="__main__": 
   Driver()          # call Driver() function