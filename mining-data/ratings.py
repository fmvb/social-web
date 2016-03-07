def readData():
	movies = open('movie-lens-1M/movies.dat', 'r')
	print "First line movies.dat: " + movies.readline().strip()
	movies.close()
	
	users = open('movie-lens-1M/users.dat', 'r')
	print "First line users.dat: " + users.readline().strip()
	users.close()

if __name__ == "__main__":
    print "Reading data from movielens files....."
    readData()
