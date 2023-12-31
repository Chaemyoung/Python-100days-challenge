programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

# Retrieving items from dictionary.
print(programming_dictionary["Function"])

#Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."

#Create an empty dictionary
empty_dictionary = {}

#Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
#Edit an itemin a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

################################################

#Nesting a list in a Dictionary
travel_log1 = {
    "France": ["Paris", "Lille", "Digon"]
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

#Nesting Dictionary in a Dictionary
Travel_log2 = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
}

#Nesting Dictionaries in Lists
travel_log3 = [
{
    "country": "France", 
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
},
{
    "country": "Germany",
    "cities_visited": ["berlin", "hamburg", "stuttgart"],
    "total_visits": 5
}
]

def add_new_country(name, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = name
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log1.append(new_country)

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log1[2]['country']} {travel_log1[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
