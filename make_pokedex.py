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
print(D2)

html_code = '''
    <link rel="stylesheet" href="testHome.css" />
    </head>
    <body>    
         <div class="background"></div>
         <div class="content">
         <h1>Gen 1 Pokemon</h1>
         <h3>Nathaniel Moy, Alex Zheng, Ajmira Islam</h3>
         <div class="intro-text">
             <p>
             An introduction to Pokemon, as if you the viewer didn't already know what that was.
             </p>
             <h3>Snorlax</h3>
             <p>We chose Snorlax as our first partner pokemon because it is what we all aspire to be after our APs at Stuy, but are strictly prohibited from becoming.</p>
         </div>
         </div>
    </body>
    '''

nav_bar = '''
    <ul>
        <li><a href="testHome.html">Home</a></li>
        <li><a href="Pokedex.html">Pokedex</a></li>
        <li><a href="top10.html">Top 10</a></li>
    </ul>
'''

nav_bar_css = '''
ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background-color: transparent;
}

li {
    float: right;
}

li a {
    display: block;
    color: black;
    text-align: center;
    padding: 20px 30px;
    text-decoration: none;
    top: 0%;
    font-size: 20px;
    font-family: "Montserrat";
}

li a:hover {
    background-color: #1bb828;
}
'''

css_code = '''

@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap');

.content {
    position: relative;
    top: 100px;
    transform: none;
    color: white;
    text-align: center;
    z-index: 1;
    font-size: 50px;
    font-family: "Montserrat";
}

.intro-text {
    font-size: 0.85em;
    color: white;
    max-width: 600px;
    margin: 10px auto;
    line-height: 1.4;
}


.background {
    position: fixed;
    width: 100%;
    height: 100%;
    background: url("home.jpg") no-repeat fixed center;
    background-size: cover;
    filter: blur(8px);
    -webkit-filter: blur(8px);
    z-index: 0;
    }
    '''

with open("testHome.html", "w") as f:
    f.write('<!DOCTYPE html>\n<html lang="en">\n\t<head>\n\t\t<title>Home</title>\n')
    f.write(nav_bar)
    f.write(html_code)
    
with open("testHome.css", "w") as f:
    f.write('\n')
    f.write(css_code)
    f.write(nav_bar_css)
    
for type in D2.keys():
    with open(f"{type}.html", "w") as f:
        f.write(f"<html><head><title>{type}<title><head><html>\n")
        
with open("top10.html", "w") as f:
    f.write('<html><head><title>Top 10<title><head><html>\n')
    
with open("Pokedex.html", "w") as f:
    f.write('<html><head><title>Pokedex<title><head><html>\n')








### CODE GRAVEYARD
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