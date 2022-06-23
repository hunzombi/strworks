# strworks
# This module is about working with strings.
# Features:
    1. Makepattern - it is a class which stores the pattern.
1.1 search - checks if the pattern is in a string.                               
1.2 overwrite - works like search but also replaces the section in the text.                         
2/3 - search/overwrite - they work like the class functions but take a pattern as an agrument to.                      
4/5 - rot13_encode/rot13_decode - a simple rot13 algorithm.                                   
6/7 - rotx_encode/rotx_decode - they work like the rot13 but you can specify the number of characters to shift.                    
8 - filter_int - returns an int from all the digits in the string.                                
9 - filter_str - returns a string from all the non-digit characters in the string.                       
10 - reverse_str - reverses the string.
# Syntax:
1 - Makepattern(pattern) the pattern needs to be a string SPECIAL CHARACTERS: /d - can be any integer, /s - can be any character(str)                   
1.1 - search(text) - check for the pattern in the text.                                                         
1.2 - overwrite(text, new_text) - replace the section in text with new_text.                                    
2/3 - search(pattern, text) / overwrite(pattern, text, new_text) - same as 1.1 and 1.2.                     
4/5 - rot13_encode(text) / rot13 decode(code) - text/code to translate.                                     
6/7 - rotx_encode(text, x) / rotx_decode(code, x) - x is the number of times to shift the characters.           
8/9 - filter_int(text) / filter_str(text) - text to extract the int or string from.                
10 - reverse_str(text) - text = string you want to reverse.                                
