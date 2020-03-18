# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 22:12:31 2020

@author: Amarnath
"""

import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}
    
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)   
    
#refer https://realpython.com/python-json/
    
with open("data_file.json", "r") as read_file:
    data_1 = json.load(read_file)

print("Data is ",data_1)    

data1={
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}
    
with open("data_file1.json", "w") as write_file:
    json.dump(data1, write_file)   
    
#refer https://realpython.com/python-json/
    
with open("data_file1.json", "r") as read_file:
    data_2 = json.load(read_file)

print("\nData is ",data_2)   