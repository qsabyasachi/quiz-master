# from pymongo import MongoClient

# client = MongoClient("mongodb://127.0.0.1:27017")
# db = client.testdb
#
# cars = [ {'name': 'Audi', 'price': 52642},
#     {'name': 'Mercedes', 'price': 57127},
#     {'name': 'Skoda', 'price': 9000},
#     {'name': 'Volvo', 'price': 29000},
#     {'name': 'Bentley', 'price': 350000},
#     {'name': 'Citroen', 'price': 21000},
#     {'name': 'Hummer', 'price': 41400},
#     {'name': 'Volkswagen', 'price': 21600} ]
#
# with client:
#
#     db = client.testdb
#     db.cars.insert_many(cars)
#
# with client:
#
#     db = client.testdb
#
#     cars = db.cars.find()
#
#     for car in cars:
#         print('{0} {1}'.format(car['name'],
#             car['price']))

