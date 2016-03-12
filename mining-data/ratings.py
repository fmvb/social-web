import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def readData(filename):
    fs = open('dataset/' + filename + '.dat', 'r')    
    
    if filename == 'users':
        data = [line.strip().split('::', 3) for line in fs]
        for record in data:
            del record[-1]
    elif filename == 'movies':
        data = []
        for line in fs:
            parts = line.strip().split('::')
            parts[2] = parts[2].split('|')
            data.append(parts)
    elif filename == 'ratings':
        data = [line.strip().split('::') for line in fs]
        for record in data:
            del record[-1]    
    
    fs.close()                                        
    return data
    
def trimLists(users, ratings):
    for u in users:
        del u[-1]    # remove last column: zipcode
        del u[-1]    # remove last column: occupation
    
    for r in ratings:
        del r[-1]    # remove last column: timestamp  
    
if __name__ == "__main__":
    users   = readData('users')
    movies  = readData('movies')
    ratings = readData('ratings')
    #trimLists(users, ratings)
        
    #nrFemale = sum(1 for x in users if x[1] == 'F')
    #nrMale   = len(users) - nrFemale
    #print 'Female users: ' + `nrFemale` + '   (' + `len(users)` + ' total users)'
    #print 'Male   users: ' + `nrMale`   + '   (' + `len(users)` + ' total users)'
    
    print users[0]
    print movies[0]
    print ratings[0]
