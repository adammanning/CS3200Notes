1. **User**
	- A human being who is using the application

1. **Registration**
	- Creating an account
	1. Things needed to Register
		1. User name or email
			- Something the user knows
			- Unique id
		1. Encrypted Password
			- Secret
			- Something the user knows
			- <u>Not</u> guessable
		1. Name, etc.
			- Enhances the user's experience

1. **Authentication**
	- Verifying that a person is who they say you are
	- Verification of identity
	- Ways of Authentication
		1. Password
		1. Text Message
		1. Fingerprint
		1. Many more
	- Sign In
		- What is your id?
		- What is your password?
	- Only a person who has registered should be able to authenticate

1. **Authorization**
	- Do you have permission to do what you're trying to do

1. **Stateless**
	- HTTP is a stateless protocol
	- You're the same faceless person you were a minute ago to the server
	- The server has no idea if you're the same person
	- The server cannot discriminate between clients

1. **Browser**
	- Keeper of cookies

1. **Session**
	- Consecutive amount of time that a user spends using an application
	- Some information stored in order for the server to know who you are

1. **Cookie**
	- A file containing data/information about the user stored by the browser
	- COOKIES ARE SECURE
	- Without cookies, servers wouldn't be able to remember who you are
	- If a server sends you a cookie, the browser always sends the cookies back to the server with any requests

1. **HACK**
	- Cookies allow us to have a session
	- Not so much a hack, rather it's more like a technique

"There are two hard things in computer science..."

## Resources
- User
- Session

## PassLib
Use PassLib for password encryption

Install:
- pip install passlib[bcrypt]


Usage:
- from passlib.hash import bcrypt
- hash = bcrypt.hash("penguin") # ONLY USED FOR REGISTERING
