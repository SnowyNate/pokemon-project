from pprint import pprint
#paste the output (or pipe the output) of this program to the pokedex.html file.

text = open('pokemon.csv').read().strip().split('\n')

#print(text)

#str-> 2D list
#takes a string and turns this into a 2D list where they are first separated by line then by spaces
#first 5 items should look like:
#Author is Alex
'''
[['#', 'Name', 'Type 1', 'Type 2', 'Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation', 'Legendary'],
['1', 'Bulbasaur', 'Grass', 'Poison', '318', '45', '49', '49', '65', '65', '45', '1', 'False'],
['2', 'Ivysaur', 'Grass', 'Poison', '405', '60', '62', '63', '80', '80', '60', '1', 'False'],
['3', 'Venusaur', 'Grass', 'Poison', '525', '80', '82', '83', '100', '100', '80', '1', 'False'],
['4', 'Charmander', 'Fire', '', '309', '39', '52', '43', '60', '50', '65', '1', 'False']]
'''

def make_list(s):
    data = []
    for pokemon in s:
        data.append(pokemon.split(','))
    return data

pokemon_list = make_list(text)

print(pokemon_list[:5])

#Author is Alex (mine got overwritten :( )
#list -> dictionary
#takes a 2d list and returns a dictionary in a dictionary (Alex cooked it and did one in a dictionary in a dictionary)
#It also assigns parts of the header to the actual value
#Originally:
'''
{'Grass': {'Bulbasaur':['#: 1', 'Name: Bulbauaur'....}....}
'''
#now:
'''
{'Grass':{'Bulbasaur': {'#': '1', 'Name': 'Bulbasaur',...}...}...}
'''

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

# =====================NAV BAR========================
# Author: Ajmira
# dictionary -> html code
# Writes the code for a navbar given a dictionary
# Should show the navbar as well as a dropdown section, clicking on a section will take you to the respective page

nav_bar_css = '''
nav {
  top: 0;
  left: 0;
  width: 100%;
  background-color: rgba(255, 255, 255, 0.1); 
  backdrop-filter: blur(4px);
  z-index: 10;
  position: relative;
}
nav ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: flex-end;
}

nav ul li {
  position: relative;
  z-index: 1000; 
}

nav ul li a {
  display: block;
  color: white;
  padding: 20px 30px;
  text-decoration: none;
  font-size: 20px;
  font-family: "Montserrat";
  z-index: 1000; 
}

nav ul li:hover > a {
  background-color: #1bb828;
}

nav ul li ul.dropdown {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  background-color: #333;
  min-width: 160px;
  z-index: 9999; 
  flex-direction: column;
}

nav ul li:hover ul.dropdown {
  display: flex;
}

nav ul li ul.dropdown li a {
  color: white;
  padding: 12px 16px;
  background-color: #333;
  text-align: left;
  z-index: 1000; 
}

nav ul li ul.dropdown li a:hover {
  background-color: #1bb828;
}
'''

def create_nav(D2):
    html = "<nav><ul>"
    html += "<li><a href='Home.html'>Home</a></li>"
    html += "<li><a href='#'>Types</a><ul class='dropdown'>"

    for x in D2.keys():
        html += f"<li><a href='{x}.html'>{x}</a></li>"

    html += "</ul></li>"  # close dropdown
    html += "<li><a href='top10.html'>Top 10</a></li>"
    html += "<li><a href='Pokedex.html'>Pokedex</a></li>"
    html += "</ul></nav>"
    return html

# =====================END NAV BAR========================

# ======================HOME PAGE========================

home_html = '''
    <link rel="stylesheet" href="Home.css" />
    </head>
    <body>
         <div class="background"></div>
         <div class="content">
         <h1>Gen 1 Pokemon</h1>
         <h3>Nathaniel Moy, Alex Zheng, Ajmira Islam</h3>
         <div class="intro-text">
             <p>
             A reference guide for 151 pokemon characters of varying types and categories. This guide comes with multiple sections, a whole Pokedex for all 151 characters, a Top 10 section of our personally curated selection of pokemon, and sections for each type of pokemon.
             </p>
             <div style="height:300px;"></div>
             <h3>Snorlax</h3>
             <p>We chose Snorlax as our first partner pokemon because it is what we all aspire to be after our APs at Stuy, but are strictly prohibited from becoming.</p>
         </div>
         </div>
    </body>
    '''

home_css = '''
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap');

html, body {
    margin: 0;
    padding: 0;
    height: 100%;
    overflow-x: hidden;
    overflow-y: auto;
    background: transparent;
}


.background {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: url("home.jpg") no-repeat center center fixed;
    background-size: cover;
    filter: blur(8px);
    -webkit-filter: blur(8px);
    z-index: -1;
}

.content {
    position: relative;
    padding-top: 100px;
    color: white;
    text-align: center;
    z-index: 1;
    font-size: 50px;
    font-family: "Montserrat";
    overflow: visible; 
}

.intro-text {
    font-size: 0.75em;
    color: white;
    max-width: 1000px;
    margin: 300px auto 200px;
    line-height: 1.4;
}
'''

#Nate wrote these codes (hey they count as functions!!)
#writes files needed for the project
# thats it! it should open new files!!
with open("Home.html", "w") as f:
    f.write('<!DOCTYPE html>\n<html lang="en">\n\t<head>\n\t\t<title>Home</title>\n')
    f.write(create_nav(D2))
    f.write(home_html)

with open("Home.css", "w") as f:
    f.write('\n')
    f.write(home_css)
    f.write(nav_bar_css)

# ======================END HOME PAGE========================

# =====================POKEDEX========================
# utilizes pokemon_list from line 14
# some code was inspired/debugged by AI or StackExchange
headers = pokemon_list[0]
rows = pokemon_list[1:]

with open('pokedex.html', 'w') as file:
    file.write("<!DOCTYPE html>\n<html>\n<head>\n<title>All Pokemon</title>\n</head>\n<body>\n<h1>All Pokemon</h1>\n<table border='1' style='border-collapse: collapse;'>\n")
    file.write("<tr>")
    for header in headers:
        file.write(f"<th style='padding: 5px;'>{header}</th>")
    file.write("</tr>\n")
    for row in rows:
        file.write("<tr>")
        for cell in row:
            file.write(f"<td style='padding: 5px;'>{cell}</td>")
        file.write("</tr>\n")
    file.write("</table>\n</body>\n</html>")

# ======================END POKEDEX========================

# =====================TYPE========================
for type in D2:
    pokemons = D2[type]
    with open(type + ".html", "w") as f:
        f.write("<!DOCTYPE html>\n<html>\n<head>\n<title>" + type + " Type Pokemon</title>\n</head>\n<body>\n")
        f.write("<h1>" + type + " Type Pokemon</h1>\n")
        if len(pokemons) > 0:
            headers = list(list(pokemons.values())[0].keys())
            f.write("<table border='1' style='border-collapse: collapse;'>\n<tr>")
            for header in headers:
                f.write("<th style='padding: 5px;'>" + header + "</th>")
            f.write("</tr>\n")
            for name in pokemons:
                pokemon = pokemons[name]
                f.write("<tr>")
                for header in headers:
                    f.write("<td style='padding: 5px;'>" + pokemon[header] + "</td>")
                f.write("</tr>\n")
            f.write("</table>\n")
        else:
            f.write("<p>No Pokemon of this type.</p>\n")
        f.write("</body>\n</html>")

# =====================END TYPE========================

with open("top10.html", "w") as f:
    f.write('<html><head><title>Top 10<title><head><html>\n')








### CODE GRAVEYARD
# list -> dictionary
#function turns a 2D list into a dictionary where keys are types and values are list of a lists of characters
#[['Hello'],['So','fun!'],['This','should','work!']['1']] ->
#{Grass:[[1,'Bulbauser',...]...]}
#Author is Ajmira

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