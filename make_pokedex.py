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

# ====================ALL POKEMON========================
# utilizes pokemon_list from line 14
# some code was inspired/debugged by AI or StackExchange
headers = pokemon_list[0]
rows = pokemon_list[1:]

with open('all.html', 'w') as file:
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

css_code = '''
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
    font-size: 0.85em;
    color: white;
    max-width: 600px;
    margin: 10px auto;
    line-height: 1.4;
}
'''


#Author is Ajmira
#dictionary-> html code
#function writes the code for a navbar given a dictionary
#how is a test supposed to work for this????
#should show the navbar and dropdown and clicking on it will take you to the respective page
def create_nav(D2):
    html = "<nav><ul>"
    html += "<li><a href='testHome.html'>Home</a></li>"
    html += "<li><a href='#'>Types</a><ul class='dropdown'>"

    for x in D2.keys():
        html += f"<li><a href='{x}.html'>{x}</a></li>"

    html += "</ul></li>"  # close dropdown
    html += "<li><a href='top10.html'>Top 10</a></li>"
    html += "<li><a href='Pokedex.html'>Pokedex</a></li>"
    html += "</ul></nav>"
    return html

#Nate wrote these codes (hey they count as functions!!)
#writes files needed for the project
# thats it! it should open new files!!
with open("testHome.html", "w") as f:
    f.write('<!DOCTYPE html>\n<html lang="en">\n\t<head>\n\t\t<title>Home</title>\n')
    f.write(create_nav(D2))
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