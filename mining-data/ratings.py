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
        movie  = []
        genres = []
        for line in fs:
            parts = line.strip().split('::')
            genres.append(list(parts[0]) + parts[2].split('|'))
            movie.append((parts[0], parts[1]))
        data = (movie, genres)
    elif filename == 'ratings':
        data = [line.strip().split('::') for line in fs]
        for record in data:
            del record[-1]      #remove column timestamp
    
    fs.close()                                        
    return data
    
if __name__ == "__main__":
    users          = readData('users')
    movies, genres = readData('movies')
    ratings        = readData('ratings')
    
    for i in range(2):
        print users[i]
        print movies[i]
        print genres[i]
        print ratings[i]
        if i < len(range(2))-1:
            print '-------------------------------------------------'
