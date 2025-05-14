from pprint import pprint
#paste the output (or pipe the output) of this program to the pokedex.html file.

text = open('pokemon.csv').read().strip().split('\n')

#print(text)

def make_list(s):
    data = []
    for pokemon in s:
        data.append(pokemon.split(','))
    return data

pokemon_list = make_list(text)

def turn_dict(twodlist):
    d = {}
    headers = twodlist[0]
    
    for row in twodlist[1:]:  
        data = row  
        name = data[1]  
        type1 = data[2]
        type2 = data[3]
        
        if type1 not in d:
            d[type1] = {}
        d[type1][name] = dict(zip(headers, data))
        
        if type2 != "''":
            if type2 not in d:
                d[type2] = {}
            d[type2][name] = dict(zip(headers, data))

    return d

two = turn_dict(pokemon_list)
pprint(two)