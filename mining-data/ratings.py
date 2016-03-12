import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def readData(filename):
    fs = open('dataset/' + filename + '.dat', 'r')    
    
    if filename == 'users':
        data = [line.strip().split('::', 3) for line in fs]
        for record in data:
            del record[-1]      # remove columns occupation and zipcode
    elif filename == 'movies':
        data = []               
        for line in fs:
            parts = line.strip().split('::')
            parts[2] = parts[2].split('|')
            data.append(parts)
    elif filename == 'ratings':
        data = [line.strip().split('::') for line in fs]
        for record in data:
            del record[-1]      #remove column timestamp
    
    fs.close()                                        
    return data
    
if __name__ == "__main__":
    users   = readData('users')
    movies  = readData('movies')
    ratings = readData('ratings')
    
    # Example of counting users per gender
    #nrFemale = sum(1 for x in users if x[1] == 'F')
    #nrMale   = len(users) - nrFemale
    #print 'Female users: ' + `nrFemale` + '   (' + `len(users)` + ' total users)'
    #print 'Male   users: ' + `nrMale`   + '   (' + `len(users)` + ' total users)'
    
    # Printing first values to varify data reads
    print users[0]
    print movies[0]
    print ratings[0]
