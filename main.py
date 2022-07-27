import matplotlib.pyplot as plt
import numpy as np


pets = [
    {"name":"Blacky",
     "race":"Labrador",
     "birthdate":"2022-01-01",
     "gender":"M",
     "age":1,
     "description":"Perro",
     "location":"Tuxtla",
     "image_url":"https://www.fundacion-affinity.org/sites/default/files/los-10-sonidos-principales-del-perro.jpg"},
    {"name":"Drogo",
     "race":"Chihuahua",
     "birthdate":"2015-01-01",
     "gender":"M",
     "age":7,
     "description":"Perro",
     "location":"Tuxtla",
     "image_url":"https://www.fundacion-affinity.org/sites/default/files/los-10-sonidos-principales-del-perro.jpg"},
    {"name":"Boby",
     "race":"Chihuahua",
     "birthdate":"2008-01-01",
     "gender":"M",
     "age":14,
     "description":"Perro",
     "location":"Tuxtla",
     "image_url":"https://www.fundacion-affinity.org/sites/default/files/los-10-sonidos-principales-del-perro.jpg"},

    {"name":"Luna",
     "race":"Maltés",
     "birthdate":"2021-01-01",
     "gender":"H",
     "age":1,
     "description":"Perro",
     "location":"Tuxtla",
     "image_url":"https://www.fundacion-affinity.org/sites/default/files/los-10-sonidos-principales-del-perro.jpg"},

    {"name":"Axel",
     "race":"Chihuahua",
     "birthdate":"2022-01-01",
     "gender":"M",
     "age":1,
     "description":"Perro",
     "location":"Tuxtla",
     "image_url":"https://www.fundacion-affinity.org/sites/default/files/los-10-sonidos-principales-del-perro.jpg"},
]


def get_data():
    pets_age = []
    pets_race = []
    
    for pet in pets:
        pets_age.append(pet["age"])
        pets_race.append(pet["race"])
    pets_race_set = set(pets_race)
    return pets_age, pets_race, pets_race_set

if __name__ == '__main__':
    pets_age, pets_race, pets_race_set = get_data()
    plt.figure(figsize=(9, 2))
    plt.subplot(131)
    plt.hist(pets_age,bins=[0,2,4,6,8,10,12,14,16])
    pets_race_count = []
    for item in pets_race_set:
        pets_race_count.append(pets_race.count(item))
    plt.subplot(132)
    plt.bar(list(pets_race_set),pets_race_count)
    plt.show()