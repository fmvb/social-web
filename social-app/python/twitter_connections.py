from optparse import OptionParser
import twitter_auth as tw_auth
#import twitter
import tweepy

def readData(filename):
    data = []
    try:
        fs = open('../' + filename, 'r')
        try:
            firstline = fs.readline()
            for line in fs:
                name, account, rest = line.strip().split(',', 2)
                if (name != '' and account !=''):
                    data.append((name, account))
        finally:
            fs.close()
    except IOError:
        print 'Error opening file' + filename 
        return    
    return data

def print_accounts(account_list):
    for name, account in account_list:
        print name + ': ' + account

if __name__ == "__main__":
    parser = OptionParser()
    parser.set_defaults(filename='twitter_auth_file')
    parser.add_option('-f', '--file', dest='filename',
                  help='File to use for twitter authentication')
    (options, args) = parser.parse_args()
    
    twitter_api = tw_auth.twitter_authenticate(options.filename)
    if (twitter_api == None):
        print 'Error in authentication, exiting program.'
        exit(1)
        
    account_list = readData('tni-staff.csv')
    
    #for user in tweepy.Cursor(twitter_api.followers, screen_name=account_list[0][1]).items(200):
        #print user.screen_name
    
    #print "found %d followers" % (len(query))
    
