# Twitter v192
By Sahitya Senapathy<br>CIS 192, Fall 2020

## Extra Credit

I implemented a follower-following system 
to make up for the lost time. I also had a ton of fun making the front-end look
non-crappy :)

## Routes

- /: main view of all tweets/hashtags
- /admin: admin view
- /accounts: contains routes to /login_view and /signup_view
- /login_view: log in route
- /signup_view: sign up route  
- /logout_view: log out route
- /profile/author: profile of user with username author
- /hashtag?id=[hashtag.id]: hashtag page with given id
- /follow/author: route to follow a user with username author
- /unfollow/author: route to unfollow a user with a username author
- /delete?id=[tweet.id]: delete a Tweet with given id
- /like?id=[tweet.id]: like a Tweet with given id