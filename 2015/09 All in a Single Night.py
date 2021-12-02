# -*- coding: UTF8 -*-

def calc_all_routes(moved_from = '', distance = 0, full_route = '', hop = 1):

    if hop == 8:
        routes[full_route] = distance
        # print(full_route, distance)
    
    else:

        for city in cities:
            if full_route.find(city) == -1:
                if full_route == '':
                    calc_all_routes(city, 0, city)
                else:
                    calc_all_routes(city, distance + distances[moved_from + ' to ' + city], full_route + ' -> ' + city, hop + 1)

distances = {}
cities = []

routes = {}

file = open('.data/09 input.txt', 'r', encoding='utf8') 
for line in file:
    line = line.rstrip('\n')
    direction, distance_str = line.split(' = ')
    city_from, city_to = direction.split(' to ')
    distances[direction] = int(distance_str)
    distances[city_to + ' to ' + city_from] = int(distance_str)

    if city_from not in cities:
        cities.append(city_from)

    if city_to not in cities:
        cities.append(city_to)

calc_all_routes()

min_route = min(routes.keys(), key=(lambda k: routes[k]))
# print(min_route, routes[min_route])
print(routes[min_route])

max_route = max(routes.keys(), key=(lambda k: routes[k]))
# print(max_route, routes[max_route])
print(routes[max_route])


