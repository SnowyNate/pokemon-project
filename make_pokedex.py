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

def dict2(twodic):
    d = {}
    headers = twodic[0]
    
    for row in twodic[1:]:  
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

D2 = dict2(pokemon_list)
pprint(D2)
'''
def turn_dict(twodlist):
    d = {}
    twodlist.pop(0)
    for x in twodlist:
        if x[2] in d:
            d[x[2]].append(x)
        else:
            d[x[2]]=[x]
        if x[3] != '':
            if x[3] in d:
                d[x[3]].append(x)
            if not(x[3] in d):
                d[x[3]]=[x]
    return d

two = turn_dict(pokemon_list)
pprint(two)
'''
with open("pokemon.html", "w") as f:
    f.write('<html><head><title>Pokedex<title><head><html>\n')
    
for type in D2.keys():
    with open(f"{type}.html", "w") as f:
        f.write(f"<html><head><title>{type}<title><head><html>\n")
        
with open("top10.html", "w") as f:
    f.write('<html><head><title>Top 10<title><head><html>\n')

