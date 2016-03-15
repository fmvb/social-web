import twitter_auth as tw_auth

if __name__ == "__main__":
    twitter_api = tw_auth.twitter_authenticate('twitter_auth_file')
    if (twitter_api == None):
        print 'Error in authentication, exiting program.'
        exit(1)
        
    
