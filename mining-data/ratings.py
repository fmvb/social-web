def readData(filename):
    fs = open('dataset/' + filename + '.dat', 'r')    
    data = [line.strip().split('::') for line in fs]  
    fs.close()                                        
    return data                                       
	
if __name__ == "__main__":
    # Read data from files
    users   = readData('users')
    movies  = readData('movies')
    ratings = readData('ratings')
    
