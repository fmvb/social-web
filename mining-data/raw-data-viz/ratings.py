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
        movie = []
        movie_genre = []
        for line in fs:
            parts   = line.strip().split('::')
            movieId = parts[0]
            title   = parts[1]
            genres  = parts[2].split('|')
            for genre in genres:
                movie_genre.append((movieId, genre))
            movie.append((movieId, title))
        data = (movie, movie_genre)
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
