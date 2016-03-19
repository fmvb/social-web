import sys
from optparse import OptionParser
import tweepy

def twitter_authenticate(auth_file):
    CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET = '', '', '', ''
    
    try:
        fs = open(auth_file, 'r')
        
        try:
            split = fs.readline().strip().split(',')    
            if (split[0] == 'CONSUMER_KEY'):
                CONSUMER_KEY = split[1].strip()
            else:
                print 'Error in CONSUMER_KEY. Check authentication file \'' + auth_file + '\'.'
                return            
                    
            split = fs.readline().strip().split(',')    
            if (split[0] == 'CONSUMER_SECRET'):
                CONSUMER_SECRET = split[1].strip()
            else:
                print 'Error in CONSUMER_SECRET. Check authentication file \'' + auth_file + '\'.'
                return
                
            split = fs.readline().strip().split(',')    
            if (split[0] == 'ACCESS_TOKEN'):
                ACCESS_TOKEN = split[1].strip()
            else:
                print 'Error in ACCESS_TOKEN. Check authentication file \'' + auth_file + '\'.'
                return
                
            split = fs.readline().strip().split(',')    
            if (split[0] == 'ACCESS_TOKEN_SECRET'):
                ACCESS_TOKEN_SECRET = split[1].strip()
            else:
                print 'Error in ACCESS_TOKEN_SECRET. Check authentication file \'' + auth_file + '\'.'
                return
        finally:
            fs.close()
    except IOError:
        print 'Error in opening file ' + auth_file
        return
    
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    
    return tweepy.API(auth)

if __name__ == "__main__":
    parser = OptionParser()
    parser.set_defaults(filename='twitter_auth_file')
    parser.add_option('-f', '--file', dest='filename',
                  help='File to use for twitter authentication')
    (options, args) = parser.parse_args()
    
    twitter_api = twitter_authenticate(options.filename)
