from optparse import OptionParser
import twitter_auth as tw_auth
import tweepy
import time

def readData(filename):
    data = {}
    try:
        fs = open('../' + filename, 'r')
        try:
            firstline = fs.readline()
            for line in fs:
                name, account, rest = line.strip().split(',', 2)
                if (name != '' and account !=''):
                    data[account[1:]] = name
        finally:
            fs.close()
    except IOError:
        print 'Error opening file' + filename 
        return    
    return data

def print_accounts(dict):
    for key, value in dict.iteritems():
        print key + ': ' + value

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
        
    account_dict = readData('test-staff.csv')
    print `len(account_dict)` + ' people with twitter account in file test-staff.csv'
    #print_accounts(account_dict)
        
    test_account = 'marleenhuysman'
    followers = []
    for i, user in enumerate(tweepy.Cursor(twitter_api.followers, screen_name=test_account, count=200).pages()):
        print 'Getting followers page %i for account %s' % (i, test_account)
        followers.extend(user)
        time.sleep(60)
            
    connections = []
    print `len(followers)` + ' followers found for ' + test_account
    for user in followers:
        if user.screen_name in account_dict:
            connections.append((user.screen_name, account_dict[user.screen_name]))
    
    print `len(connections)` + ' connections found for '  + test_account + ':'
    if len(connections) > 0:
        for account, name in connections:
            print account + '\t\t' + name  
