import instaloader
L = instaloader.Instaloader()

# Login or load session
L.login("userID", "Password")        # (login)
# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, "zeus2.0._")

# Print list of followees
follow_list = []

for followee in profile.get_followers():
    follow_list.append(followee.username)
following=[]
for followee in profile.get_followees():
    following.append(followee.username)
    print (followee)
for followee in follow_list:
    if followee not in following:
        print (followee)
        print (1)
    
