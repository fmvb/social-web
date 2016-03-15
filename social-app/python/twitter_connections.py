import twitter_auth as tw_auth
import twitter

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


if __name__ == "__main__":
    #twitter_api = tw_auth.twitter_authenticate('twitter_auth_file')
    #if (twitter_api == None):
        #print 'Error in authentication, exiting program.'
        #exit(1)
        
    account_list = readData('tni-staff.csv')
    
    for name, account in account_list:
        print name + ': ' + account
        
