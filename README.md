# Twitter
Simple application like "Twitter" using Python and Django.

Application allows register user with e-mail instead username and login. After that users can adds tweets, writes comments and sends messages to other users. App is also provided with admin panel that enables managing of DB content and allows to block(as admin action) inappropriate content (tweets, comments, messages) or unblock them. Application also allows changing password and informations about user or delete account.

#### Default localhost pages:
* localhost:8000/admin - shows admin page
* localhost:8000/twitter/login/ - shows page with login form
* localhost:8000/twitter/logout/ - shows page with logout view and link to login page
* localhost:8000/twitter/signup/ - shows page with signup (automatically login user, if e-mail doesn't exist id DB)
* localhost:8000/twitter/ - shows index page with all tweets order by creation date and form to create new tweet
* localhost:8000/twitter/tweet_details/{tweet_id}/ - shows page with tweet's details and comment form
* localhost:8000/twitter/user_details/{user_id}/ - shows page with user's details and button to send message
* localhost:8000/twitter/user_update/{user_id}/ - shows page with logged user's details and update informations form
* localhost:8000/twitter/password_change/ - shows page with password change form
* localhost:8000/twitter/password_change/done/ - shows this page if password has been changed successfully
* localhost:8000/twitter/user_delete/ - delete logged user's account
* localhost:8000/twitter/messages/ - shows page with received (shows information if message is unread) and sent messages
* localhost:8000/twitter/message_details/{message_id}/ - shows page with message's details
* localhost:8000/twitter/add_message/{user_id} - shows page with form to send new message from curently logged user.
