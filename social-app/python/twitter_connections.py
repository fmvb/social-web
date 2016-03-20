from optparse import OptionParser
import twitter_auth as tw_auth
import tweepy
import time
import os

def read_data(filename):
    name_dict, id_dict = {}, {}
    dict_count = 0
    try:
        fs = open('../' + filename, 'r')
        try:
            fs.readline()       # header line contains no account info
            for line in fs:
                name, account, rest = line.strip().split(',', 2)
                if (name != '' and account !=''):
                    name_dict[account[1:]] = name
                    id_dict[account[1:]]   = dict_count
                    dict_count += 1
        finally:
            fs.close()
    except IOError:
        print 'Error opening file ' + filename 
        return    
    return (name_dict, id_dict)

def read_progress(filename):
    progress = set()
    if os.path.isfile(filename):
        try:
            fs = open(filename, 'r')
            try:
                for line in fs:
                    key = line.strip()
                    progress.add(key)
            finally:
                fs.close()
        except IOError:
            print 'Error opening progress file ' + filename 
            return    
    return progress
                
def get_followers(account):
    followers = []
    for i, page in enumerate(tweepy.Cursor(twitter_api.followers, screen_name=account, count=200).pages()):
        print 'Getting followers page %d' % (i+1)
        followers.extend(page)
        time.sleep(60)
    return followers

def get_connections(followers):
    connections = []    
    for user in followers:
        if user.screen_name in account_dict:
            connections.append((user.screen_name, account_dict[user.screen_name]))
    return connections

def write_connections(connections, source, account_dict, id_dict):
    nodes, edges = 'nodes.csv', 'edges.csv'
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
        
def write_progress(account):
    fs = open('progress.csv', 'a') # append account to progress file
    fs.write('%s\n' % account)
    fs.close()
    
def write_error(account):
    fs = open('error.csv', 'a') # append account to progress file
    fs.write('%s\n' % account)
    fs.close()
    
if __name__ == "__main__":
    parser = OptionParser()
    parser.set_defaults(authfile='twitter_auth_file', input_file='tni-staff.csv')
    parser.add_option('-a', '--auth', dest='authfile',
                  help='File to use for twitter authentication')
    parser.add_option('-f', '--file', dest='input_file',
                  help='Input file with staff accounts')              
    (options, args) = parser.parse_args()
    
    twitter_api = tw_auth.twitter_authenticate(options.authfile)
    if (twitter_api == None):
        print 'Error in authentication, exiting program.'
        exit(1)
        
    account_dict, id_dict = read_data(options.input_file)
    print `len(account_dict)` + ' people with twitter account in file ' + options.inputfile
    
    progress = read_progress('progress.csv')
        
    for account in account_dict:    
        if account not in progress:
            print '\nAccount: ' + account
            try:
                followers = get_followers(account)
                print `len(followers)` + ' followers found'
                    
                connections = get_connections(followers)    
                print `len(connections)` + ' NI-connections found'
            
                if len(connections) > 0:
                    write_connections(connections, account, account_dict, id_dict)
                write_progress(account)
            except tweepy.TweepError:
                print 'Error while fetching followers'
                write_error(account)
        else:
            print 'Connections already harvested for ' + account
