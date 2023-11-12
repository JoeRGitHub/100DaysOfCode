country = input("Add country name: ") # Add country name
visits = int(input("Number of visits: ")) # Number of visits
#Works only when I use the x ver, I didn't exactly understand what the 'eval' does
list_of_cities = eval(input("create list from formatted string: ")) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆
#list_of_cities = list_of_cities.split(', ')
# TODO: Write the function that will allow new countries
# to be added to the travel_log. 

def add_new_country(new_country_name, num_of_visits, list_of_cities):
    #A way to enforce my lack of understanding on func 'eval'
    #x = list(list_of_cities.split(" ")) # 
    new_country = {}
    new_country['country'] = new_country_name
    new_country['visits'] = num_of_visits
    #new_country["cities"] = x
    new_country['cities'] = list_of_cities
    travel_log.append(new_country)

# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
print(travel_log)

 
