from optparse import OptionParser
import twitter_auth as tw_auth
import tweepy
import time
import os

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
        print 'Getting followers page %d' % i
        followers.extend(user)
        time.sleep(60)
    return followers

def get_connections(followers):
    connections = []    
    for user in followers:
        if user.screen_name in account_dict:
            connections.append((user.screen_name, account_dict[user.screen_name]))
    return connections

def write_connections(connections, source, account_dict, id_dict):
    nodes, edges = 'twitter-nodes.csv', 'twitter-edges.csv'
    fsn = open(nodes, 'a+') # reading and appending
    fse = open(edges, 'a+') # reading and appending   
    
    if os.stat(nodes).st_size == 0:
        fsn.write('id,name\n')
    if os.stat(edges).st_size == 0:
        fse.write('source,target\n')
    
    fsn.write('%d,%s\n' % (id_dict[source], account_dict[source]))
    for target, name in connections:
        fse.write('%d,%d\n' % (id_dict[source], id_dict[target]))
    print 'Written connections to csv files'
    
    fsn.close()
    fse.close()

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
        
    account = 'marleenhuysman'
    print 'Account: ' + account
    followers = get_followers(account)
    print `len(followers)` + ' followers found'
            
    connections = get_connections(followers)    
    print `len(connections)` + ' NI-connections found'
    
    if len(connections) > 0:
        write_connections(connections, account, account_dict, id_dict)
