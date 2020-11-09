"""Contador de palabras: actualizar el script 
anterior que lea un archivo de texto y retorne las 10 palabras más 
repetidas. Usando clases, métodos, instancias y lo previamente visto 
en clase."""

import re as regex
import operator
import sys


class WordsCounter:

    def __init__(self, list_words):
        
        self.list_words = list_words
      
    def show_name(self):
        
          print("[ * ] File has been selected: [", self.list_words, "]\n")
             
    def count(self, num = 10):
            
        while True:
            
                try:
                    
                    _list_words = []
                    _list_counter = []
                    
                    with open(self.list_words) as my_file:
                        
                        for line in my_file:
                            
                            words = regex.findall(r"\S+", line)
                            _list_words += words
                            
                        _list_counter = list(map(lambda item : _list_words.count(item), _list_words))
                    
                    dict_words = dict(list(zip(_list_words, _list_counter)))  
                    words_sort = dict(sorted(dict_words.items(), key = operator.itemgetter(1), reverse = True))
                    
                    print("       Words        |          Count     ")
                    for key, value in words_sort.items():
                        
                        if num > 0:
                            print("==================================================")
                            print("|       ",key,"        |       ",value, "       |")
                            print("==================================================")
                            
                            num -= 1
                            
                    print("\n")       
                    print("[ o ] End list")
                    print("==================================================")
                    print("\n")
                       
                    print("[ ! ] Press < Enter > to return \n")
                    input("WordsCounter >>> ")
                    break
                
                except:
                    
                    sys.exit("[ ! ] [Error: This file can't be reader.]") 