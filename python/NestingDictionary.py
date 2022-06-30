
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",

# }

# travel_log = {
#     "France": {"cities_Visited":["Paris", "Lile", "Dijon",], "total_visits": 12},
#     "Germany":{"cities_Visited":["Berlin", "Hamburg", "Stuttgart"],"total_visits": 15}    
# }


#dictionary inside list 

travel_log = [
    {
    "country": "France",
     "total_visits": 12,
     "cities_Visited":["Paris", "Lile", "Dijon",],
    },
     {
    "country": "Germany",
     "total_visits": 15,
     "cities_Visited":["Berlin", "Hamburg", "Stuttgart",],
    }
]

def add_new_country(country_name, number_visit, cities):
    new_country ={}
    new_country["country"] = country_name
    new_country["total_visits"] = number_visit
    new_country["cities_visited"] = cities
    travel_log.append(new_country)
 

add_new_country("Russia", 2, ["Moscow","Saint Peterburg"])
add_new_country("Philippines", 10, ["Cavite","Manila"])
print(travel_log)