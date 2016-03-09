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
    
    # remove occupation and zipcode from users
    for user in users:
        del user[-1]    # remove last column: zipcode
        del user[-1]    # remove last column: occupation
