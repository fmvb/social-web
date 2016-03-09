def readData(filename):
    fs = open('dataset/' + filename + '.dat', 'r')    
    data = [line.strip().split('::') for line in fs]  
    fs.close()                                        
    return data
    
def trimLists(users, ratings):
	# remove occupation and zipcode from users
    for u in users:
        del u[-1]    # remove last column: zipcode
        del u[-1]    # remove last column: occupation
    
    # remove timestamps from ratings
    for r in ratings:
        del r[-1]    # remove last column: timestamp  
    
if __name__ == "__main__":
    # Read data from files
    users   = readData('users')
    movies  = readData('movies')
    ratings = readData('ratings')
    trimLists(users, ratings)
        
    nrFemale = sum(1 for x in users if x[1] == 'F')
    nrMale   = len(users) - nrFemale
    print 'Female users: ' + `nrFemale` + '   (' + `len(users)` + ' total users)'
    print 'Male   users: ' + `nrMale`   + '   (' + `len(users)` + ' total users)'
        
    
    
