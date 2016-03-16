import sys
from optparse import OptionParser
import twitter

def twitter_authenticate(auth_file):
    CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET = '', '', '', ''
    
    try:
        fs = open(auth_file, 'r')
        
        try:
            split = fs.readline().strip().split(',')    
            if (split[0] == 'CONSUMER_KEY'):
                CONSUMER_KEY = split[1]
            else:
                print 'Error in CONSUMER_KEY. Check authentication file \'' + auth_file + '\'.'
                return            
                    
            split = fs.readline().strip().split(',')    
            if (split[0] == 'CONSUMER_SECRET'):
                CONSUMER_KEY = split[1]
            else:
                print 'Error in CONSUMER_SECRET. Check authentication file \'' + auth_file + '\'.'
                return
                
            split = fs.readline().strip().split(',')    
            if (split[0] == 'OAUTH_TOKEN'):
                CONSUMER_KEY = split[1]
            else:
                print 'Error in OAUTH_TOKEN. Check authentication file \'' + auth_file + '\'.'
                return
                
            split = fs.readline().strip().split(',')    
            if (split[0] == 'OAUTH_TOKEN_SECRET'):
                CONSUMER_KEY = split[1]
            else:
                print 'Error in OAUTH_TOKEN_SECRET. Check authentication file \'' + auth_file + '\'.'
                return
        finally:
            fs.close()
    except IOError:
        print 'Error in opening file ' + auth_file
        return
    
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

if __name__ == "__main__":
    parser = OptionParser()
    parser.set_defaults(filename='twitter_auth_file')
    parser.add_option('-f', '--file', dest='filename',
                  help='File to use for twitter authentication')
    (options, args) = parser.parse_args()
    
    twitter_api = twitter_authenticate(options.filename)
