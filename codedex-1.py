# 01. Hi Bestie!

# Write code below 💖

genz_slang = ['bestie', 'tea', 'cap', 'sus']

print(genz_slang)


# codedex 

# Hi Bestie 👋
# Codédex

# Define a list with slang terms
genz_slang_list = [
    'bestie',
    'tea',
    'cap'
]

# Iterate over the list and print the slangs
for term in genz_slang_list:
    print(term)

# Define a dictionary with slang terms and meanings
genz_slang_dict = {
    "bestie": "best friend or new friend",
    "tea": "news or gossip"
}

# Print the slang terms and their meanings
for term, meaning in genz_slang_dict.items():
    print(f"{term}: {meaning}")

# Uncomment for alternative example
    
# for term, meaning in genz_slang.items():
    # Print the slang term followed by its meaning
    # print(term, ":", meaning)
    # print()  # Add an empty line for readability


# 02. Find My Friends

# Write code below 💖

city=('juangadh',)
f1=(51.507351,-0.127758)
f2=(15.870032,100.992538)
f3=(22.441650,73.866890)

print("Latitude and Longitude of the furthest friend's location:", f1)
ft = f1 + f2 + f3
print("All friends' locations combined:", ft)
1

# 03. Met Museum

# Write code below 💖

information = {'artis':'Unknown','period':'late Iron Age','date':'ca. 60 BCE'}

print(information)
print(information.keys())
print(information.values())
print(information.items())


# girhub codedex

# Met Museum 🖼️
# Codédex

# Dictionary representing a Pyxis (with some extra info)
pyxis = {
  'artist': 'Penthesilea painter',
  'period': 'classical',
  'date': '465-460 BCE',
  'culture': ['Greek', 'Attic'],
  'medium': ['terracotta', 'white-ground'],
  'dimensions': {'height': '4.75in', 'height w/cover': '6.75in'}
}

print('Printing the dictionary: ', pyxis)
print('\nPrinting the keys: ', pyxis.keys())
print('\nPrinting the values: ', pyxis.values())

# 04. Fruit Cart

# Write code below 💖

set1 = {'banana','apple','guava'}
set2 = {'apple','pineapple','papaya'}

print(set1)
print(set2)

set_union=set1.union(set2)
set_intersection=set1.intersection(set2)
set_difference=set1.difference(set2)
print(set_union)
print(set_intersection)
print(set_difference)


# codedex github

# Fruit Cart 🍓
# Codédex

my_fruits = {'apple', 'banana', 'kiwi'}
friend_fruits = {'banana', 'orange', 'grape'}

# Uncomment to check if a fruit is <in> both list
# print('apple' in fruits)  # Output: True
# set3 = {'apple', 'orange'}
# print(set3.issubset(fruits))  # Output: True

union_result = my_fruits | friend_fruits
intersection_result = my_fruits & friend_fruits
difference_result = my_fruits - friend_fruits

print('Union:', union_result)
print('Intersection:', intersection_result)
print("My Fruits - Friend's Fruits:", difference_result)

# 05. Post-Game Stats 

# Post Game Stats 🏈
# Codédex

# Task 1: Create Player Data
players_data = [
    {"name": "Patrick Mahomes", "position": "Quarterback", "jersey_number": 15, "yards_gained": 400, "touchdowns": 3},
    {"name": "Tyreek Hill", "position": "Wide Receiver", "jersey_number": 10, "yards_gained": 150, "touchdowns": 2},
    # Add more players as needed
]
names = [player["name"] for player in players_data]
print("Players Names:", names)

# Task 2: Analyze Player Positions
positions = [player["position"] for player in players_data]
print("Player Positions:", positions)

# Task 3: Update Player Statistics
players_data[0]["yards_gained"] += 50
players_data[0]["touchdowns"] += 1

# Task 4: Calculate Average Stats
average_yards = sum(player["yards_gained"] for player in players_data) / len(players_data)
average_touchdowns = sum(player["touchdowns"] for player in players_data) / len(players_data)
print("Average Yards Gained:", average_yards)
print("Average Touchdowns:", average_touchdowns)