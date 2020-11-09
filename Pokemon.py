import requests as req
import json
import operator
import sys

api_url = "https://pokeapi.co/api/v2/pokemon/?offset=0&limit=20"

class Pokemon():
    
    def __init__(self):
         pass
     
    #Obtengo un json a partir de una api
    def get_json(self , url):
        try:
            res = req.get(url)
            
            json_data = res.json()
            
            json_data_ = json.dumps(json_data, indent = 4)
            
            json_data = json.loads(json_data_)
         
        except:
            print("Error:")
        else:
            
            return json_data
        
     #REgresa una lista con el nombre y la url de cada poke   
    def get_name(self):
        
        poke_name = []
        
        try:
            
            poke_json = self.get_json(api_url)
         
        except:
            
            print("Error:")
        else:
            
            for poke in poke_json['results']:
                
                poke_name.append(poke['name'])
                
            return poke_name
    
    def get_stats_hp(self):
        
        while True:
            try:
                
                pokemons_name = []
                hp_pokes_arr = []
                num = 20
                for item in range(1, 20):
                    pkm = self.get_json('https://pokeapi.co/api/v2/pokemon/{0}'.format(item))
                    hp_pokes_arr.append(pkm['stats'][0]['base_stat']) 
                
                for poke_name in self.get_name():
                    pokemons_name.append(poke_name)
                #
                dict_pokemons = dict(list(zip(pokemons_name, hp_pokes_arr)))
                order_pokemons = dict(sorted(dict_pokemons.items(), key = operator.itemgetter(1), reverse = True))
                
                print("       Name        |          HP     ")
                for key, value in order_pokemons.items():
                    
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
                input("Pokemon >>> ")
                break
        
            except:
                
                sys.exit("[ ! ] [Error: This file can't be reader.]") 
    
    
    def get_stats_attack(self):
        
        while True:
            try:
                
                pokemons_name = []
                att_pokes_arr = []
                num = 20
                for item in range(1, 20):
                    pkm = self.get_json('https://pokeapi.co/api/v2/pokemon/{0}'.format(item))
                    att_pokes_arr.append(pkm['stats'][1]['base_stat']) 
                
                for poke_name in self.get_name():
                    pokemons_name.append(poke_name)
                #
                dict_pokemons = dict(list(zip(pokemons_name, att_pokes_arr)))
                order_pokemons = dict(sorted(dict_pokemons.items(), key = operator.itemgetter(1), reverse = True))
                
                print("       Name        |       Attack     ")
                for key, value in order_pokemons.items():
                    
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
                input("Pokemon >>> ")
                break
        
            except:
                
                sys.exit("[ ! ] [Error: This file can't be reader.]") 
    
    def get_stats_defence(self):
        
        while True:
            try:
                
                pokemons_name = []
                def_pokes_arr = []
                num = 20
                for item in range(1, 20):
                    pkm = self.get_json('https://pokeapi.co/api/v2/pokemon/{0}'.format(item))
                    def_pokes_arr.append(pkm['stats'][2]['base_stat']) 
                
                for poke_name in self.get_name():
                    pokemons_name.append(poke_name)
                #
                dict_pokemons = dict(list(zip(pokemons_name, def_pokes_arr)))
                order_pokemons = dict(sorted(dict_pokemons.items(), key = operator.itemgetter(1), reverse = True))
                
                print("       Name        |          Defence     ")
                for key, value in order_pokemons.items():
                    
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
                input("Pokemon >>> ")
                break
        
            except:
                
                sys.exit("[ ! ] [Error: This file can't be reader.]") 
