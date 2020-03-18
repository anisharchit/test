# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 22:20:46 2020

@author: Amarnath
"""

# Python3 program to illustrate store  
# efficiently using pickle module  
# Module translates an in-memory Python object  
# into a serialized byte stream—a string of  
# bytes that can be written to any file-like object. 
  
import pickle 
  
def storeData(): 
    # initializing data to be stored in db 
    Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak', 
    'age' : 21, 'pay' : 40000} 
    Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak', 
    'age' : 50, 'pay' : 50000} 
  
    # database 
    db = {} 
    db['Omkar'] = Omkar 
    db['Jagdish'] = Jagdish 
      
    # Its important to use binary mode 
    dbfile = open('examplePickle', 'ab') 
      
    # source, destination 
    pickle.dump(db, dbfile)                      
    dbfile.close() 
  
def loadData(): 
    # for reading also binary mode is important 
    dbfile = open('examplePickle', 'rb')      
    db = pickle.load(dbfile) 
    for keys in db: 
        print(keys, '=>', db[keys]) 
    dbfile.close() 
  
if __name__ == '__main__': 
    storeData() 
    loadData() 
    
"""
Pickle Vs JSON

Advantages of using Pickle Module:

Recursive objects (objects containing references to themselves): Pickle keeps track of the objects it has already serialized, so later references to the same object won’t be serialized again. (The marshal module breaks for this.)
Object sharing (references to the same object in different places): This is similar to self- referencing objects; pickle stores the object once, and ensures that all other references point to the master copy. Shared objects remain shared, which can be very important for mutable objects.
User-defined classes and their instances: Marshal does not support these at all, but pickle can save and restore class instances transparently. The class definition must be importable and live in the same module as when the object was stored.