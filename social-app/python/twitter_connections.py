from optparse import OptionParser
import twitter_auth as tw_auth
import tweepy
import time

def readData(filename):
    name_dict, id_dict = {}, {}
    dict_count = 0
    try:
        fs = open('../' + filename, 'r')
        try:
            firstline = fs.readline()
            for line in fs:
                name, account, rest = line.strip().split(',', 2)
                if (name != '' and account !=''):
                    name_dict[account[1:]] = name
                    id_dict[account[1:]]   = dict_count
                    dict_count += 1
        finally:
            fs.close()
    except IOError:
        print 'Error opening file' + filename 
        return    
    return (name_dict, id_dict)

def get_followers(username):
    followers = []
    for i, user in enumerate(tweepy.Cursor(twitter_api.followers, screen_name=username, count=200).pages()):
        print 'Getting followers page %i for account %s' % (i, username)
        followers.extend(user)
        time.sleep(60)
    return followers

def get_connections(followers):
    connections = []    
    for user in followers:
        if user.screen_name in account_dict:
            connections.append((user.screen_name, account_dict[user.screen_name]))
    return connections

def write_connections(connections, id, user):
    fsn = open('twitter-nodes.csv', 'a')
    fse = open('twitter-edges.csv', 'a')
    
    if fsn.readline() is None:
        fsn.write('id,name,group\n')
        fse.write('source,target\n')
    else:
        fsn.write(id, user)
        #for account, name in connections:
            

def print_accounts(dict):
    for key, value in dict.iteritems():
        print key + ': ' + `value`

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
        
    account_dict, id_dict = readData('test-staff.csv')
    print `len(account_dict)` + ' people with twitter account in file test-staff.csv'
    #print_accounts(id_dict)
        
    test_account = 'marleenhuysman'
    #followers = get_followers(test_account)
    #print `len(followers)` + ' followers found for ' + test_account
            
    #connections = get_connections(followers)    
    #print `len(connections)` + ' connections found for '  + test_account + ':'
    #for screen_name, name in connections:
    #    print '(' + screen_name + ', ' + name + ')'
        
