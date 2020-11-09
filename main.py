import WordsCounter as wc
import Pokemon as pk
import StatusBar as sb
import os
from random import randint

files = ["info.txt", "ML.txt", "Pokemon.txt"]
_banner = ["logo.txt", "logopy.txt", "logoLI.txt"]
poke_opt = ["HP", "Attack", "Defence"]


if __name__ == '__main__':
           
    while True:
            
        try: 
            
            with open(_banner[randint(0, 2)]) as logo:
                for line in logo: 
                    print(line,end="")
                  
            print("=============================")
            print("Select a file to read")
            print("=============================")
            print("\n")
            
            k=0
            for ele in files: 
                print('[',k,']',ele) 
                k+=1
            print("[ x ] Exit \n") 
            
            file_name = input("WordsCounter >>> ")
            print("\n")
            
            if file_name == 'x':
                print("[ ! ] Are you sure? [ y/n ] \n")
                res = input("WordsCounter >>> ")
                print("\n")
                
                if res == 'y':
                    print("[ o ] Ending... \n")
                    break
                elif res == 'n':
                    print("\n")
                    continue
                else:
                    print("=============================")
                    print("[ ! ] Unrecognized Command.")
                    print("=============================")
                    print("\n")
                    print("=============================")
                    print("\n")
                    continue
            
            
            if file_name >= 'a':
                
                print("[ ! ] Enter a number or < x > to finish.")
                continue 
            
            else:
                if files[int(file_name)] in files:
                    
                    """Poke Api"""  
                            
                    while True:
                            
                        if files[int(file_name)] == 'Pokemon.txt':
                            
                            with open('bannerpk.txt') as logo:
                                for line in logo: 
                                    print(line,end="")
                            
                            
                            print("=============================")
                            print("Select Option")
                            print("=============================")
                            print("\n")
                            
                            i=0
                            for ele in poke_opt: 
                                print('[',i,']',ele) 
                                i+=1
                            print("[ x ] Back \n") 
                            option = input("Pokemon >>> ")
                            print("\n")
                            
                            
                            if option == 'x':
                                print("[ ! ] Are you sure? [ y/n ] \n")
                                res = input("Pokemon >>> ")
                                print("\n")
                                
                                if res == 'y':
                                    print("[ o ] Ending... \n")
                                    break
                                elif res == 'n':
                                    print("\n")
                                    continue
                                else:
                                    print("=============================")
                                    print("[ ! ] Unrecognized Command.")
                                    print("=============================")
                                    print("\n")
                                    print("=============================")
                                    print("\n")
                                    continue
                            if file_name >= 'a':
                        
                                print("[ ! ] Enter a number or < x > to finish.")
                                continue
                            else:    
                                _pk = pk.Pokemon()
                                sb.StatusBar()
                                
                                if int(option) == 0:
                                    _pk.get_stats_hp()
                                elif int(option) == 1:      
                                    _pk.get_stats_attack()
                                elif int(option) == 2:      
                                    _pk.get_stats_defence()
                                    
                        else:
                            
                    
                
                            if os.stat(files[int(file_name)]).st_size != 0: 
                            
                                _wc = wc.WordsCounter(files[int(file_name)]) 
                                _wc.show_name()
                                
                                print("=============================")
                                print("[ * ] How many words do you want? \n")
                                quantity = int(input("WordsCounter >>> "))
                                print("\n")
                                
                                sb.StatusBar()
                                
                                if quantity > 0:
                                    
                                    _wc.count(quantity)
                                    break
                                else:
                                    
                                    print("=============================")
                                    print("[ ! ] The number must be bigger than < 0 >\n")
                                    print("[ ! ] By default only 10 words will be displayed\n")
                                    
                                    _wc.count()
                                    break
                            else:
                                print("[ ! ] File empty, try again.\n")
                                print("[ ! ] Press < Enter > to return \n")
                                input("WordsCounter >>> ")  
                                print("\n")
                                break
                else:
                    print("[ ! ] File Unknown, try again.\n")
                    
        except:
            print("=============================")
            print("[ ! ] Error: Unrecognized Command.")
            print("=============================")
            