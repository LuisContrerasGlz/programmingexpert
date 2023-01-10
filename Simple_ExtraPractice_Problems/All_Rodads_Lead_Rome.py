"""

You are given a list with various flight connections in Europe. Each connection is represented as a tuple with the following elements:

(city_from, city_to, time)

For example, the following tuple represents a flight from Amsterdam to Dublin which takes 100 minutes:

('Amsterdam', 'Dublin', 100)

Your task is to go through all routes in a loop and check how many of them lead to Rome (i.e. how many of them have city_to equal to 'Rome'). Among the routes to Rome, you should also calculate the average flight time. Print the following no the output:

{} connections lead to Rome with an average flight time of {} minutes

Replace {} with the number of connections. and the average flight time.

"""

connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170)
]

counter = 0
sum = 0.0

for con in connections:
    if con[1] == 'Rome':
        counter += 1
        sum += con[2]

print(counter, 'connections lead to Rome with an average flight time of',
      sum/counter, 'minutes')
